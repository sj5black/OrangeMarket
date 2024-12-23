from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import get_user_model
from django.db.models import Q, Count

from .forms import ArticleForm, CommentForm
from .models import Article, Comment, Hashtag

def articles(request):
    sort_by = request.GET.get('sort_by', 'date')
    articles = Article.objects.all()
    
    # 인기도, 최신순 정렬
    if sort_by == 'popularity':
        articles = articles.annotate(like_count=Count('like_users')).order_by('-like_count', '-created_at')
    elif sort_by == 'date':
        articles = articles.order_by('-created_at')
    else:
        articles = articles.order_by("-id")
    
    # 검색어 처리
    query = request.GET.get('q', '')  # 검색어 가져오기
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |  # 제목에 검색어 포함
            Q(content__icontains=query) |  # 내용에 검색어 포함
            Q(author__username__icontains=query) |  # 판매자 이름에 검색어 포함
            Q(hashtags__name__icontains=query)  # 해시태그에 검색어 포함
        ).distinct()  # 중복상품 방지

    context = {"articles": articles, "query": query, "sort_by": sort_by}
    return render(request, "articles/articles.html", context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.view_count += 1
    article.save()
    
    comment_form = CommentForm()
    comments = article.comments.all().order_by("id")
    total_comments = article.comments.count()
    context = {
        "article" : article, 
        "comment_form" : comment_form,
        "comments" : comments,
        "total_comments" : total_comments,
        }
    return render(request, "articles/article_detail.html", context)

def add_hashtags_to_article(article, hashtags):
    valid_hashtags = set()  # set을 사용하여 중복 해시태그 제거
    for hashtag in hashtags:
        hashtag = hashtag.strip()
        if hashtag and hashtag.startswith("#"):  # '#'이 포함된 해시태그만 처리
            valid_hashtags.add(hashtag)  # 유효한 해시태그만 set에 추가

    # 해시태그 객체가 이미 존재하는지 한 번만 확인하고, 필요한 해시태그를 생성
    existing_hashtags = Hashtag.objects.filter(name__in=valid_hashtags)
    existing_hashtags_set = set(existing_hashtags.values_list('name', flat=True))

    new_hashtags = valid_hashtags - existing_hashtags_set  # 새로 추가해야 할 해시태그
    hashtag_objects_to_create = [Hashtag(name=hashtag) for hashtag in new_hashtags]

    # 새 해시태그가 있으면 한 번에 추가
    if hashtag_objects_to_create:
        Hashtag.objects.bulk_create(hashtag_objects_to_create)

    # 기존 해시태그 객체와 새로 생성된 해시태그 객체 연결
    for hashtag_name in valid_hashtags:
        hashtag_obj, created = Hashtag.objects.get(name=hashtag_name)
        article.hashtags.add(hashtag_obj)  # Hashtag 객체를 Article에 추가

        
@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            # 해시태그 처리
            hashtags = form.cleaned_data['hashtags']
            for hashtag in hashtags:
                # 이미 존재하는 해시태그를 가져오거나 새로 생성
                hashtag_obj, created = Hashtag.objects.get_or_create(name=hashtag)
                # article과 해당 해시태그 연결
                article.hashtags.add(hashtag_obj)
            return redirect("articles:article_detail", article.id)
    else:
        form = ArticleForm()
    context = {"form": form}
    return render(request, "articles/create.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.author:
        return redirect("articles:articles")
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            # 기존 해시태그 삭제
            article.hashtags.clear()
            # 새 해시태그 추가
            hashtags = form.cleaned_data['hashtags']
            for hashtag in hashtags:
                # 이미 존재하는 해시태그를 가져오거나 새로 생성
                hashtag_obj, created = Hashtag.objects.get_or_create(name=hashtag)
                # article과 해당 해시태그 연결
                article.hashtags.add(hashtag_obj)
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {"form": form, "article": article}
    return render(request, "articles/update.html", context)



@login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if request.user == article.author:
            # 게시글에 사용된 해시태그가 다른 게시글에서 사용되지 않는 경우 삭제
            for hashtag in article.hashtags.all():
                if hashtag.articles.count() == 1:  # 다른 게시글에서 사용되지 않음
                    hashtag.delete()
            article.delete()  # 게시글 삭제

    return redirect("articles:articles")

@login_required
@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.author = request.user
        comment.save()
    return redirect("articles:article_detail", article.pk)

@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect("articles:article_detail", article_pk)

@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
        else:
            article.like_users.add(user)
        return redirect("articles:articles")
    return redirect("accounts:login")

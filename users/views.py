from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from accounts.forms import ProfilePictureForm
from articles.models import Article

# def users(request):
#     return render(request, "users/users.html")

def profile(request, username):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    member = get_object_or_404(get_user_model(), username=username)
    
    # 사용자가 자신의 프로필을 보는 경우에만 사진 업데이트 가능
    if request.user == member:
        if request.method == 'POST':
            form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('users:profile', username=username)  # 프로필 페이지 새로고침
        else:
            form = ProfilePictureForm(instance=request.user)
    else:
        form = None  # 다른 사용자의 프로필에서는 업데이트 폼을 비활성화
        
    member_articles = Article.objects.filter(author=member)
    liked_articles = Article.objects.filter(like_users=member)
    
    context = {
        "member": member,
        "member_articles": member_articles,
        "liked_articles": liked_articles,
    }
    return render(request, "users/profile.html", context)

@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    else:
        return redirect("accounts:login")
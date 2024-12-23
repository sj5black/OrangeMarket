from django import forms
from .models import Article, Comment, Hashtag
import re

class ArticleForm(forms.ModelForm):
    hashtags = forms.CharField(
        max_length=500,
        required=False,
        help_text="해시태그를 공백으로 구분하여 입력하세요. (예: #패션 #가방 #클러치)"
    )

    class Meta:
        model = Article
        fields = ['title', 'content', 'image']  # 필요한 필드만 명시, 'hashtags'는 별도 처리
        exclude = ['author']  # author는 자동 설정되므로 제외

    def __init__(self, *args, **kwargs):
        # 기존 해시태그를 폼에 전달
        article_instance = kwargs.get('instance')
        if article_instance and article_instance.pk:
            # 기존 해시태그를 폼에 전달하여 초기값 설정
            initial_hashtags = " ".join([f"{hashtag.name}" for hashtag in article_instance.hashtags.all()])
            kwargs.update({'initial': {'hashtags': initial_hashtags}})
        
        super().__init__(*args, **kwargs)
        
    def clean_hashtags(self):
        hashtags_input = self.cleaned_data['hashtags']
        
        # #을 기준으로 분리하고, 특수문자나 공백을 만날 때까지 처리
        hashtags = []
        current_hashtag = ""
        in_hashtag = False  # 해시태그가 시작되었는지 여부

        for char in hashtags_input:
            if char == '#':  # #을 만나면 새로운 해시태그 시작
                if current_hashtag:  # 이전 해시태그가 있으면 저장
                    hashtags.append(current_hashtag.strip())
                current_hashtag = "#"  # #은 항상 포함되도록 처리
                in_hashtag = True
            elif in_hashtag:
                if char.isalnum() or char == '_':  # 알파벳, 숫자, _만 허용
                    current_hashtag += char  # 유효한 문자라면 해시태그에 추가
                else:  # 특수문자나 공백을 만나면 해시태그를 저장하고 종료
                    hashtags.append(current_hashtag.strip())
                    current_hashtag = ""
                    in_hashtag = False

        # 마지막 해시태그가 남아있는 경우 추가
        if current_hashtag:
            hashtags.append(current_hashtag.strip())

        # 유효성 검사 후, 해시태그 저장
        valid_hashtags = []
        for hashtag in hashtags:
            if hashtag:  # 빈 문자열은 무시
                valid_hashtags.append(hashtag)

        return valid_hashtags

    def save(self, commit=True):
        article = super().save(commit=False)  # Article 객체를 저장하기 전에 commit=False로 호출
        if commit:
            article.save()  # DB에 Article 객체 저장
            hashtags = self.cleaned_data.get('hashtags', [])

            # 기존 해시태그와 새로운 해시태그 연결 처리
            for hashtag_name in hashtags:
                hashtag_obj, created = Hashtag.objects.get_or_create(name=hashtag_name)
                article.hashtags.add(hashtag_obj)  # ManyToMany 관계 추가

        return article
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article","author",)


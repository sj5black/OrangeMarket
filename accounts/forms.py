from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")
    
    # 각 필드에 대한 추가 설정 (옵션)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True  # 이메일 필수 입력
        self.fields['email'].label = "E-mail Address"  # 이메일 라벨 설정
        self.fields['first_name'].required = False  # First Name 선택 입력
        self.fields['first_name'].label = "First Name"  # 라벨 변경
        self.fields['last_name'].required = False  # Last Name 선택 입력
        self.fields['last_name'].label = "Last Name"  # 라벨 변경
        
class CustomUserChangeForm(UserChangeForm):
    # password = None
    class Meta:
        model = get_user_model() # 현재 활성화된 유저 접근
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text
            
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_picture']
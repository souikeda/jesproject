from django import forms
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from internalusers.models import User

class ExternalUserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'ログイン'))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("ログイン情報が正しくありません。")
            if user.user_type != 1:  # 外部ユーザのみ許可
                raise forms.ValidationError("外部ユーザではありません。")
        return self.cleaned_data

User = get_user_model()

class ExternalUserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)  # E-mailを必須にする
    company_name = forms.CharField(label='会社名', max_length=255, required=True)  # 会社名を必須にする

    class Meta:
        model = User
        fields = ['company_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # E-mailがユニークであることを確認
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("このEメールアドレスは既に登録されています。")
        return email

    def clean_company_name(self):
        company_name = self.cleaned_data.get('company_name')
        # name（usernameの代わり）フィールドがユニークであることを確認
        if User.objects.filter(name=company_name).exists():
            raise forms.ValidationError("この会社名は既に登録されています。")
        return company_name

    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data['company_name']  # nameに会社名を設定
        user.email = self.cleaned_data['email']  # Emailを保存
        user.user_type = 1  # 外部ユーザとしてuser_typeを1に設定
        if commit:
            user.save()
        return user
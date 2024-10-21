# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ExternalUserLoginForm, ExternalUserRegisterForm
from internalusers.auth_backends import ExternalUserBackend


def external_login_view(request):
    if request.method == 'POST':
        form = ExternalUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password, backend='internalusers.auth_backends.ExternalUserBackend')  # 外部ユーザ用バックエンドを指定
            if user:
                login(request, user)
                return redirect('external_dashboard')
    else:
        form = ExternalUserLoginForm()

    return render(request, 'externalusers/external_login.html', {'form': form})


def external_register_view(request):
    if request.method == 'POST':
        form = ExternalUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])  # パスワードをハッシュ化
            user.save()
            return redirect('externalusers:external_login')  # 登録後にログインページへリダイレクト
    else:
        form = ExternalUserRegisterForm()
    
    return render(request, 'externalusers/external_register.html', {'form': form})
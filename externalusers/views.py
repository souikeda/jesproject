from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  # authenticateのインポート
from .forms import ExternalUserLoginForm

from .forms import RegisterForm

def external_login_view(request):
    if request.method == 'POST':
        form = ExternalUserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('external_dashboard')  # 外部ユーザ用のダッシュボードへリダイレクト
    else:
        form = ExternalUserLoginForm()

    return render(request, 'external_login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
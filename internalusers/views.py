from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import InternalUserLoginForm

def internal_login_view(request):
    if request.method == 'POST':
        form = InternalUserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['name'], password=form.cleaned_data['password'])
            if user is not None and user.user_type == 2:  # 内部ユーザか確認
                login(request, user)
                return redirect('internal_dashboard')
    else:
        form = InternalUserLoginForm()
    return render(request, 'internal_login.html', {'form': form})

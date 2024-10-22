from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# 外部ユーザ専用のダッシュボード
@login_required(login_url=reverse_lazy('externalusers:external_login'))
def dashboard_view(request):
    # ログインセッションが有効で、外部ユーザの場合にのみヘッダーを表示
    header_visible = request.user.is_authenticated and request.user.user_type == 1

    context = {
        'header_visible': header_visible,
    }
    return render(request, 'jesapp/dashboard.html', context)

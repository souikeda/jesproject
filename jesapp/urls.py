from django.urls import path
from . import views

# アプリケーション名を指定
app_name = 'jesapp'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),  # ダッシュボード用のURL
]

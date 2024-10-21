from django.urls import path
from .views import external_login_view, external_register_view
from django.contrib.auth import views as auth_views

app_name = 'externalusers'

urlpatterns = [
    path('login/', external_login_view, name='external_login'),
    path('register/', external_register_view, name='external_register'),
    
    # パスワードリセットのURLパターン
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

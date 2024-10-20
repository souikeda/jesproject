from django.urls import path
from .views import internal_login_view

app_name = 'internalusers' # 名前空間を定義

urlpatterns = [
    path('login/', internal_login_view, name='internal_login'),
]

from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# デバッグ用に開発環境の設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

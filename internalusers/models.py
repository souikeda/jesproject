from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator

# ローマ字と数字のみ、4桁以上10桁以下のバリデーション
alphanumeric_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9]{4,10}$',
    message='Name must be 4-10 characters long and contain only letters and numbers.'
)

class CustomUserManager(BaseUserManager):
    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('Nameは必須です')
        extra_fields.setdefault('user_type', 2)  # スーパーユーザは内部ユーザとして設定
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, 'external'),
        (2, 'internal'),
    )
    name = models.CharField(
        max_length=10,
        unique=True,
        validators=[alphanumeric_validator],  # バリデーションを追加
        help_text='4-10 characters, letters and numbers only'
    )
    email = models.EmailField(blank=True, null=True)  # Emailは必須ではない
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'  # Nameでログイン
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class JesUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Userテーブルと1:1のリレーション
    department = models.CharField(max_length=200)
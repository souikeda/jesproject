from django.db import models
from internalusers.models import User

class TMstCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Userテーブルとの1:1リレーション
    nameryaku = models.CharField(max_length=200, null=True, blank=True)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    telno = models.CharField(max_length=15, null=True, blank=True)

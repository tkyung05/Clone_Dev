from django.db import models


class Account(models.Model):
    name = models.CharField(max_length = 30)
    profile = models.ImageField(upload_to = 'images/user_profile/%Y/%m/%d', blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
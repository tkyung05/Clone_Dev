from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=50, null=False)
    uesr_image = models.ImageField(upload_to = 'images/blog/profile_image/%Y/%m/%d', null=False)
    photo = models.ImageField(upload_to = 'images/blog/%Y/%m/%d') 
    hash_tag = models.CharField(max_length=30) 
    content = models.TextField()
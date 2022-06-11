from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=50, null=True, default="someone")
    photo = models.ImageField(upload_to = 'images/blog/%Y/%m/%d') 
    hash_tag = models.CharField(max_length=30) 
    content = models.TextField() 

    
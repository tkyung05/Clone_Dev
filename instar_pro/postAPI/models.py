from django.db import models


class Post(models.Model):
    photo = models.ImageField(upload_to = 'images/%Y/%m/%d') 
    hash_tag = models.CharField(max_length=30, blank=True) 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    
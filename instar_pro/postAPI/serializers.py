from dataclasses import field
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'profile_image', 'photo','hash_tag', 'content',]

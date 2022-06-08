from rest_framework import serializers
from .models import Post


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'photo','hash_tag', 'content', 'created_at']
from django.views import View
from rest_framework import viewsets
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny

from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


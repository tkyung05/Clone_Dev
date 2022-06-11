from django.urls import path
from . import views 

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = [
    path('', post_list),
]
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('UserAPI.urls')),
    path('post/', include('postAPI.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Django

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from posts import views as posts_views

urlpatterns = [
    path("posts/", posts_views.list_post),
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
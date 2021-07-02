# Django

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

# Local Apps
from users import views as user_views
from posts import views as posts_views

urlpatterns = [
    path("posts/", posts_views.list_post, name="feed"),
    path("admin/", admin.site.urls),
    path("users/login/", user_views.login_view, name="login")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
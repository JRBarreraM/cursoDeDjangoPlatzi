"""Platzigram's URL's module"""
# Django
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from Platzigram import views as localViews
from posts import views as postViews
from users import views as users_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('posts/',postViews.list_posts,name='feed'),
    path('users/login/',users_views.login_view,name='login'),
    path('users/logout/',users_views.logout_view,name='logout'),
    path('users/signup/',users_views.signup_view,name='signup'),
    path('users/me/profile/',users_views.update_profile,name='update_profile'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
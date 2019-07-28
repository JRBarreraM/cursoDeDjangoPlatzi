"""Platzigram's URL's module"""
# Django
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from Platzigram import views as localViews
from posts import views as postViews

urlpatterns = [
    path('admin/',admin.site.urls),
    path('posts/',postViews.list_posts)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
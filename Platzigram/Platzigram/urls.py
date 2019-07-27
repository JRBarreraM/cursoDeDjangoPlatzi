"""Platzigram's URL's module"""
# Django
from django.urls import path
from django.contrib import admin

from Platzigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/',admin.site.urls),

    path('hello-world/', local_views.helloWorld),
    path('sortIntegers/', local_views.sortIntegers),
    path('sayHi/<str:name>/<int:age>',local_views.sayHi),

    path('posts/',posts_views.list_posts),
]

"""Platzigram's URL's module"""
from django.urls import path
from Platzigram import views

urlpatterns = [
    path('hello-world/', views.helloWorld),
    path('sortIntegers/', views.sortIntegers),
    path('sayHi/<str:name>/<int:age>',views.sayHi),
]

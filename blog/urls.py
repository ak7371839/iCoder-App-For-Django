from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('bloghome', views.bloghome, name="bloghome"),
    path('search', views.search, name="search"),
    path('<str:slug>', views.blogpost, name="blogpost"),
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('handlesingup', views.handlesingup, name="handlesingup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('handlelogout', views.handlelogout, name="handlelogout"),
    path('handleblogs', views.handleblogs, name="handleblogs"),
    path('<str:slug>', views.not_found, name="not_found"),
]
from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("service/", views.nice, name="blog service"),
    path("contact", views.fly, name="blog-contants"),
]
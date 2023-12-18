from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="web-home"),
    path("about/",views.nice,name="web-nice"),
]
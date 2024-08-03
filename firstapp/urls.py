from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index-page"),
    path("main", main, name="main-page"),
    path("home", home, name="home-page"),
    path("about", about, name="about-page"),

]



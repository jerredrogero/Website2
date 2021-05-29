from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("projects/", projects, name="projects"),
    path("blog/<slug:slug>/", post_detail, name="post_detail"),
    path("category/<str:cats>/", CategoryView, name="category"),
]

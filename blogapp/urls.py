
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="blogindex"),
    path("post/",views.post,name="allpost"),
    path("post/<slug:slug>",views.postdetail,name="postdetail"),
]

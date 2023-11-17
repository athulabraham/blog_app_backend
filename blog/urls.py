from django.urls import path
from . import views

urlpatterns = [
    path("view/",views.View,name="view"),
    path("add/",views.Add,name="add"),
    path("search/",views.Search,name="search"),
    path("delete/",views.Delete,name="delete"),
    path("user/",views.User,name="user"),
]
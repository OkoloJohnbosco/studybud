from django.urls import URLPattern, path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("room/", views.room, name="room")
]

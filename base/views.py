from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {"id": 1, "name": "lets learn python"},
    {"id": 2, "name": "Design with me"},
    {"id": 3, "name": "Frontend Devs"},
]


def home(request):
    return render(request, "home.html", {"rooms": rooms})


def room(request):
    return render(request, "room.html")

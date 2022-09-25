from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

rooms = [
    {"id": 1, "name": "lets learn python"},
    {"id": 2, "name": "Design with me"},
    {"id": 3, "name": "Frontend Devs"},
]


def home(request):
    rooms = Room.objects.all()
    return render(request, "base/home.html", {"rooms": rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, "base/room.html", {"path": pk, 'room': room})

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {"id": 1, "name": "lets learn python"},
    {"id": 2, "name": "Design with me"},
    {"id": 3, "name": "Frontend Devs"},
]


def home(request):
    return render(request, "base/home.html", {"rooms": rooms})


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i['name']
    return render(request, "base/room.html", {"path": pk, 'room': room})

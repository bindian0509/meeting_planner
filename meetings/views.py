from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Meeting
from .models import Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def room(request, id):
    kamra = get_object_or_404(Room, pk=id)
    return render(request, "rooms/room.html", {"room": kamra})


def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})
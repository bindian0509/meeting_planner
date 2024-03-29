from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

# Create your views here.
from .models import Meeting
from .models import Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def room(request, id):
    kamra = get_object_or_404(Room, pk=id)
    return render(request, "rooms/room.html", {"room": kamra})


def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {"form": form})
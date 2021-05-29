from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
from meetings.models import Room


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all(),
                   "rooms": Room.objects.all()})


def date(request):
    return HttpResponse("I am welcoming you at : " + str(datetime.now()))


def about_me(request):
    return HttpResponse(
        "Hi My name is <a href='http://twitter.com/bindian0509'>@bindian0509</a> and I type things in computer for money!")

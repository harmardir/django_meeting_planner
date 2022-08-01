from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return render(request, "website/welcome.html",
    {"message": "This data was sent from the view to the template" })

def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))

def about(request):
    return HttpResponse("Hello I am Harout, I am Python developer")


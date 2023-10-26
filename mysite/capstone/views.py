from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
import datetime

def index(request):
    activity = Activity.objects.all()
    print(activity.values()[0]['ip'])
    return HttpResponse("Hello, world. You're at the capstone index.")

def insertactivity(request, ip, gyrox, gyroy, gyroz):
    print(ip, gyrox, gyroy, gyroz)
    ac = Activity(ip=ip, gyrox=gyrox, gyroy=gyroy, gyroz=gyroz, time=datetime.datetime.now())
    ac.save()
    return HttpResponse("save done")

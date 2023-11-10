from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from .models import mealAmount
import datetime
from rest_framework.response import Response

def index(request):
    activity = Activity.objects.all()
    print(activity.values()[0]['ip'])
    return HttpResponse("Hello, world. You're at the capstone index.")

def insertactivity(request, ip, Acc_x,Acc_y,Acc_z,Gyro_x, Gyro_y, Gyro_z):
    print(ip, Acc_x,Acc_y,Acc_z,Gyro_x, Gyro_y, Gyro_z)
    ac = Activity(ip=ip, Acc_x = Acc_x,Acc_y = Acc_y,Acc_z = Acc_z,Gyro_x=Gyro_x, Gyro_y=Gyro_y, Gyro_z=Gyro_z, DateTime=datetime.datetime.now())
    ac.save()
    return HttpResponse("save done")

def getmealAmount(request,ip):
    # mealAmount = calculateMealAmount()
    # TCP CLIENT한테 소켓으로 MEAL AMOUNT 전송
    print("qew")
    return Response("100")


def calculateMealAmount():
    # 디비 쿼리 호출 하고 -> 밥량 계산
    mealAmount.objects.all()
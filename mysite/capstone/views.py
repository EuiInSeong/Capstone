from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Activity
from .models import mealAmount
from .models import DogStatus
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import generics
from django.core import serializers
from django.db.models import Sum
import datetime
# import serial
import pickle
import json

def index(request):
    activity = Activity.objects.all()
    print(activity.values()[0]['ip'])
    return HttpResponse("Hello, world. You're at the capstone index.")

def insertactivity(request, ip, Acc_x,Acc_y,Acc_z,Gyro_x, Gyro_y, Gyro_z):
    print(ip, Acc_x,Acc_y,Acc_z,Gyro_x, Gyro_y, Gyro_z)
    ac = Activity(ip=ip, Acc_x = Acc_x,Acc_y = Acc_y,Acc_z = Acc_z,Gyro_x=Gyro_x, Gyro_y=Gyro_y, Gyro_z=Gyro_z, DateTime=datetime.datetime.now())
    ac.save()
    if(Activity.objects.count() % 10 == 0):
        storeStatus()
    return HttpResponse("save done")

def activity(request):
    queryset = Activity.objects.all()
    item = serializers.serialize("json", queryset)
    return HttpResponse(item, status = 200)

def status(request):
    queryset = DogStatus.objects.all()
    item = serializers.serialize("json", queryset)
    return HttpResponse(item, status = 200)

def getmealAmount(request):
    latestStatus = DogStatus.objects.order_by('-Date').first()
    dogIP = latestStatus.ip
    resultMealAmount = {"meal amount": latestStatus.accumulatedMeal}
    if(latestStatus.accumulatedMeal >= 10):
        responseData = json.dumps(resultMealAmount)
        response = HttpResponse(responseData, content_type = 'application/json')
        resetMealStatus = DogStatus(ip = dogIP, walking = 0, resting = 0, running = 0, accumulatedMeal = 0, Date = datetime.datetime.now() )
        resetMealStatus.save()
        return response
    else:
        responseData = json.dumps(resultMealAmount)
        response = HttpResponse(responseData, content_type = "application/json")
        return response
    
def insertStatus(request, ip, walking, resting, running, accumulatedMeal):
    print(ip, walking, resting, running)
    st = DogStatus(ip = ip, walking = walking, resting = resting, running = running, accumulatedMeal = accumulatedMeal, Date = datetime.datetime.now())
    st.save()
    return HttpResponse("status saved")

def calculateMealAmount():
    
    latestStatus = DogStatus.objects.order_by('-id').first()
    mealAmount += (int(latestStatus.walking)//60) + (int(latestStatus.running//30)) + (int(latestStatus.resting)//180)
    print(mealAmount)
    return mealAmount

file_path = "C:/Users/home/Downloads/model3.pkl"
with open(file_path , 'rb') as f:
    loaded_model = pickle.load(f)

def storeStatus():
    avgAcc_x = Activity.objects.all().order_by('-DateTime')[:10].aggregate(Sum('Acc_x'))['Acc_x__sum']//10
    avgAcc_y = Activity.objects.all().order_by('-DateTime')[:10].aggregate(Sum('Acc_y'))['Acc_y__sum']//10
    avgAcc_z = Activity.objects.all().order_by('-DateTime')[:10].aggregate(Sum('Acc_z'))['Acc_z__sum']//10
    avgGyro_x = Activity.objects.all().order_by('-DateTime')[:10].aggregate(Sum('Gyro_x'))['Gyro_x__sum']//10
    avgGyrp_y = Activity.objects.all().order_by('-DateTime')[:10].aggregate(Sum('Gyro_y'))['Gyro_y__sum']//10
    avgGyro_z = Activity.objects.all().order_by('-DateTime')[:10].aggregate(Sum('Gyro_z'))['Gyro_z__sum']//10
    dogIP = Activity.objects.all().order_by('-DateTime')[0].ip
    
    status = loaded_model.predict([[int(avgAcc_x),int(avgAcc_y),int(avgAcc_z),int(avgGyro_x),int(avgGyrp_y),int(avgGyro_z)]])[0]
    
    latestStatus = DogStatus.objects.order_by('-Date').first()
    latestWalk = latestStatus.walking
    latestRest = latestStatus.resting
    latestRun = latestStatus.running 
    
    latestMeal = (int(latestStatus.walking)//60) + (int(latestStatus.running//30)) + (int(latestStatus.resting)//180)
    print(status)

    st = DogStatus(ip = dogIP, walking = latestWalk, resting = latestRest, running = latestRun, accumulatedMeal = latestMeal, Date =  datetime.datetime.now())
    st.save()
    if(int(status) == 0):
        stNew = DogStatus(ip = dogIP, walking = latestWalk + 1, resting = latestRest, running = latestRun, accumulatedMeal = latestMeal, Date = datetime.datetime.now())
        stNew.save()
        print("saved")
    elif(int(status) == 1):
        stNew = DogStatus(ip = dogIP, walking = latestWalk, resting = latestRest, running = latestRun+1, accumulatedMeal = latestMeal, Date = datetime.datetime.now())
        stNew.save()
        print("saved")
    elif(int(status) == 2):
        stNew = DogStatus(ip = dogIP, walking = latestWalk, resting = latestRest+1, running = latestRun , accumulatedMeal = latestMeal, Date = datetime.datetime.now())
        stNew.save()
        print("saved")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
#     5분 - 100개 : 최소, 최대 차이 
    
#     ser = serial.Serial(
#     port = 'COM3',
#     baudrate = 9600,
# )

# def dog_data(request):
#     try:
#         data_from_arduino = ser.readline().decode("UTF-8")
#         json_data = json.loads(data_from_arduino)
        
#         new_data = Activity(
#             ip = json.data['ip'],
#             Acc_x = json.data['Acc_x'],
#             Acc_y = json.data['Acc_y'],
#             Acc_z = json.data['Acc_z'],

#             Gyro_x = json.data['Gyro_x'],
#             Gyro_y = json.data['Gyro_y'],
#             Gyro_z = json.data['Gyro_z'],
#             DateTime = datetime.datetime.now(),
#         )
#         new_data.save()
#         response_data = {"status": "success", "message": "Sensor data received and saved successfully"}
#         return JsonResponse(response_data, status=200)
#     except json.JSONDecodeError as e1:
#         error_message = f"Error decoding JSON data : {str(e1)}"
#         return JsonResponse({"status": "error", "message": error_message}, status=400)

#     except Exception as e2:
#         error_message = f"Error processing sensor data: {str(e2)}"
#         return JsonResponse({"status": "error", "message": error_message}, status=500)

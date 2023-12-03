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
    return HttpResponse(item, status=200)

def getmealAmount(request):
    latestStatus = DogStatus.objects.order_by('-id').first()
    resultMealAmount = latestStatus.values('accumulatedMeal')
    return HttpResponse(resultMealAmount)

def insertStatus(request, ip, walking, resting, running):
    print(ip, walking, resting, running)
    mealAmount = int(walking)//60 + int(running)//30 + int(resting)//180
    st = DogStatus(ip = ip, walking = walking, resting = resting, running = running, accumulatedMeal = mealAmount, Date = datetime.datetime.now())
    st.save()
    return HttpResponse("status saved")

# def calculateMealAmount():
#     # 디비 쿼리 호출 하고 -> 밥량 계산    
#     # dogStatus = DogStatus.objects.all()
    
#     latestStatus = DogStatus.objects.order_by('-id').first()
#     # mealAmount += (int(latestStatus.walking)//60) + (int(latestStatus.running//30)) + (int(latestStatus.resting)//180)
#     print(mealAmount)
#     return mealAmount

file_path = "C:/Users/home/downloads/model1 (1).pkl"
with open(file_path , 'rb') as f:
    loaded_model = pickle.load(f)

def storeStatus():
    avgAcc_x = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Acc_x'))['Acc_x__sum']//10
    avgAcc_y = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Acc_y'))['Acc_y__sum']//10
    avgAcc_z = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Acc_z'))['Acc_z__sum']//10
    avgGyro_x = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Gyro_x'))['Gyro_x__sum']//10
    avgGyrp_y = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Gyro_y'))['Gyro_y__sum']//10
    avgGyro_z = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Gyro_z'))['Gyro_z__sum']//10

    status = loaded_model.predict([[avgAcc_x,avgAcc_y,avgAcc_z,avgGyro_x,avgGyrp_y,avgGyro_z]])[0]
    print(status)
    latestStatus = DogStatus.objects.order_by('-id').first()
    latestWalk = latestStatus.walking
    latestRest = latestStatus.resting
    latestRun = latestStatus.running 
    latestMeal = latestStatus.accumulatedMeal

    print(latestMeal)
    st = DogStatus(latestStatus.ip, latestWalk, latestRest, latestRun, latestMeal, datetime.datetime.now())
    if(int(status) == 0):
        st = DogStatus(latestStatus.ip, latestWalk + 1, latestRest, latestRun, latestMeal,datetime.datetime.now())
        st.save()
    elif(int(status) == 1):
        st = DogStatus(latestStatus.ip, str(latestWalk), str(latestRest+1), str(latestRun), str(latestMeal),datetime.datetime.now())
        st.save()
    elif(int(status) == 2):
        st = DogStatus(latestStatus.ip, latestWalk, latestRest, latestRun+1, latestMeal,datetime.datetime.now())
        st.save()
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
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

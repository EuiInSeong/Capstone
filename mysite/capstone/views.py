from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Activity
from .models import mealAmount
from .models import DogStatus
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from django.core import serializers
from django.db.models import Sum
import datetime
import serial
import pickle


def index(request):
    activity = Activity.objects.all()
    print(activity.values()[0]['ip'])
    return HttpResponse("Hello, world. You're at the capstone index.")

def insertactivity(request, ip, Acc_x,Acc_y,Acc_z,Gyro_x, Gyro_y, Gyro_z):
    print(ip, Acc_x,Acc_y,Acc_z,Gyro_x, Gyro_y, Gyro_z)
    ac = Activity(ip=ip, Acc_x = Acc_x,Acc_y = Acc_y,Acc_z = Acc_z,Gyro_x=Gyro_x, Gyro_y=Gyro_y, Gyro_z=Gyro_z, DateTime=datetime.datetime.now())
    ac.save()
    return HttpResponse("save done")

def activity(request):
    queryset = Activity.objects.all()
    item = serializers.serialize("json", queryset)
    return HttpResponse(item, status=200)

def getmealAmount(request):
    resultMealAmount = calculateMealAmount()
    return HttpResponse(resultMealAmount)

def insertStatus(request, ip, walking, resting, running, accumulatedMeal):
    print(ip, walking, resting, running)
    st = DogStatus(ip = ip, walking = walking, resting = resting, running = running, accumulatedMeal = calculateMealAmount(), Date = datetime.datetime.now())
    st.save()
    if(Activity.objects.count % 10 == 0):
        storeStatus()
    return HttpResponse("status saved")

def calculateMealAmount():
    # 디비 쿼리 호출 하고 -> 밥량 계산    
    # dogStatus = DogStatus.objects.all()
    mealAmount = 0
    latestStatus = DogStatus.objects.order_by('-id').first()
    mealAmount += (int(latestStatus.walking)//60) + (int(latestStatus.running//30)) + (int(latestStatus.resting)//180)
    print(mealAmount)
    return mealAmount

file_path = './model1 (1).pkl'
with open(file_path , 'rb') as f:
    loaded_model = pickle.load(f)

def storeStatus():
    avgAcc_x = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Acc_x')) 
    avgAcc_y = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Acc_y'))
    avgAcc_z = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Acc_z'))
    avgGyro_x = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Gyro_x'))
    avgGyrp_y = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Gyro_y'))
    avgGyro_z = Activity.objects.all().order_by('-id')[:10].aggregate(Sum('Gyro_z'))

    status = loaded_model([[avgAcc_x,avgAcc_y,avgAcc_z,avgGyro_x,avgGyrp_y,avgGyro_z]])[0]
    
    latestStatus = DogStatus.objects.order_by('-id').first()
    latestWalk = int(latestStatus.walking) 
    latestRest = int(latestStatus.resting) 
    latestRun = int(latestStatus.running) 
    latestMeal = int(latestStatus.accumulatedMeal)

    st = DogStatus(latestStatus.ip, latestWalk, latestRest, latestRun, latestMeal,datetime.datetime.now())
    if(int(status) == 0):
        st = DogStatus(latestStatus.ip, str(latestWalk+1), str(latestRest), str(latestRun), str(latestMeal),datetime.datetime.now())
        st.save()
    elif(int(status) == 1):
        st = DogStatus(latestStatus.ip, str(latestWalk), str(latestRest+1), str(latestRun), str(latestMeal),datetime.datetime.now())
        st.save()
    elif(int(status) == 2):
        st = DogStatus(latestStatus.ip, str(latestWalk), str(latestRest), str(latestRun+1), str(latestMeal),datetime.datetime.now())
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
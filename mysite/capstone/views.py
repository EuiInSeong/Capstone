from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Activity
from .models import mealAmount
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializer import ActivitySerializer
from .models import Activity
import datetime

class ActivityListAPIView(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    

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
    return HttpResponse("100")

def calculateMealAmount():
    # 디비 쿼리 호출 하고 -> 밥량 계산
    mealAmount.objects.all()
    
    
    # 5분 - 100개 : 최소, 최대 차이 
    
    # ser = serial.Serial(
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

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("/",views.dog_dadog_datata, name = "dog_data"),
    path("insertactivity/<str:ip>/<str:Acc_x>/<str:Acc_y>/<str:Acc_z>/<str:Gyro_x>/<str:Gyro_y>/<str:Gyro_z>", views.insertactivity, name="insertactivity"),
    path("getmealAmount/",views.getmealAmount, name = "getmealAmount"),
    path("activity" ,views.activity, name = 'activity'),
    path("insertstatus/<str:ip>/<str:walking>/<str:resting>/<str:running>", views.insertStatus, name = "insertstatus"),   
]
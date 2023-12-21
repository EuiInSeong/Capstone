from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insertactivity/<str:ip>/<str:Acc_x>/<str:Acc_y>/<str:Acc_z>/<str:Gyro_x>/<str:Gyro_y>/<str:Gyro_z>", views.insertactivity, name="insertactivity"),
    path("getmealAmount/",views.getmealAmount, name = "getmealAmount"),
    path("activity" ,views.activity, name = 'activity'),
    path("insertstatus/<str:ip>/<str:walking>/<str:resting>/<str:running>/<str:accumulatedMeal>", views.insertStatus, name = "insertstatus"),
    path("status", views.status, name = "status"),
    path("info/<str:ip>/<str:Age>/<str:Name>/<str:Breed>/<str:Weight>/<str:Height>", views.info, name = "info"),
    path("dogSearch", views.dogSearch, name = "dogSearch"),
]
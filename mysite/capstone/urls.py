from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insertactivity/<str:ip>/<str:Acc_x>/<str:Acc_y>/<str:Acc_z>/<str:Gyro_x>/<str:Gyro_y>/<str:Gyro_z>", views.insertactivity, name="insertactivity"),
    path("getmealAmount/<str:ip>",views.getmealAmount, name = "getmealAmount")
]
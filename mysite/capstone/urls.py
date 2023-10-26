from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insertactivity/<str:ip>/<str:gyrox>/<str:gyroy>/<str:gyroz>", views.insertactivity, name="insertactivity"),
]
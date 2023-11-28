from peewee import *
from db import mysql

class BaseModel(Model):
    class Meta:
        database = mysql

class Activity(BaseModel):
    ip = CharField(max_length=100)
    Acc_x = FloatField(null=True)
    Acc_y = FloatField(null=True)
    Acc_z = FloatField(null=True)
    Gyro_x = FloatField(null=True)
    Gyro_y = FloatField(null=True)
    Gyro_z = FloatField(null=True)
    datetime = DateTimeField(null=True)

class MealAmount(BaseModel):
    ip = CharField(max_length=100)
    dogip = CharField(max_length=100)
    mealAmount = IntegerField(default=0)
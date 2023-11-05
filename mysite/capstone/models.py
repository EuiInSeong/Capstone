from django.db import models

class Activity(models.Model):
    ip = models.CharField(max_length=100, blank=True, null=True)  
    Acc_x = models.FloatField(blank=True,null=True)
    Acc_y = models.FloatField(blank=True,null=True)
    Acc_z = models.FloatField(blank=True,null=True)    
    Gyro_x = models.FloatField(blank=True, null=True)
    Gyro_y = models.FloatField(blank=True, null=True)
    Gyro_z = models.FloatField(blank=True, null=True)
    DateTime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'activity'
        managed = True


#Database table

# class mealAmount(models.Model):
#     #급식기 ip
#     ip = models.CharField(max_length = 100, blank = True,null=True)
#     id = models.CharField(max_length=100,blank = True,null=True)
#     mealAmount = models.IntegerField(default=0)
    
    
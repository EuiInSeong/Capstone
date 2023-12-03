from django.db import models

#sensor table
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
        db_table = 'Activity'
        managed = True


#status table
class DogStatus(models.Model):
    ip = models.CharField(max_length = 100, blank = True,null=True)
    walking = models.FloatField(blank = True, null = True)
    resting = models.FloatField(blank = True, null = True)
    running = models.FloatField(blank = True, null = True)
    accumulatedMeal = models.FloatField(blank = True, null = True)
    Date = models.DateTimeField(blank = True, null = True)
    
    class Meta:
        db_table = 'DogStatus'
        managed = True
        

class mealAmount(models.Model):
    #급식기 ip
    ip = models.CharField(max_length = 100, blank = True,null=True)
    DatTime = models.FloatField(blank = True, null = True)
    mealAmount = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'mealAmount'
        managed = True
    
    
    
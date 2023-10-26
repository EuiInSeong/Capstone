from django.db import models

class Activity(models.Model):
    ip = models.CharField(max_length=100, blank=True, null=True)
    gyrox = models.FloatField(blank=True, null=True)
    gyroy = models.FloatField(blank=True, null=True)
    gyroz = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'activity'
        managed = True

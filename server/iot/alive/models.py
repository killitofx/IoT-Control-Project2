from django.db import models

# Create your models here.
class Alive(models.Model):
    device_id = models.IntegerField()
    ip_address = models.CharField(max_length=25)
    times = models.IntegerField()
    send_data = models.BooleanField()
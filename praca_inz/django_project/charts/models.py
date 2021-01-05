from django.db import models
from django.utils import timezone

class UserInputDate(models.Model):
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)


class sensor_mean(models.Model):
	temperature_mean = models.FloatField()
	pressure_mean = models.FloatField()
	humidity_mean = models.FloatField()
	date_mean = models.DateField(default=timezone.now)
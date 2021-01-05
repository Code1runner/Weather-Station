from django.db import models
from django.utils import timezone
# Create your models here.

class sensor(models.Model):
	temperature = models.FloatField()
	pressure = models.FloatField()
	humidity = models.FloatField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(str(self.temperature)+','+str(self.pressure)+','+str(self.humidity)+str(self.date))
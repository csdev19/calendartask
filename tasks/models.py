from django.db import models
from schedules.models import Days

# Create your models here.
class Task (models.Model):
	task_name = models.CharField (max_length=50) 
	description = models.TextField()
	task_to_day = models.ForeignKey (Days, on_delete=models.CASCADE)

	def __str__ (self):
		return self.task_name

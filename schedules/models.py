from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class Months (models.Model):
	ENERO = 'ene'
	FEBRERO = 'feb'
	MARZO = 'mar'
	ABRIL = 'abr'
	MAYO = 'may'
	JUNIO = 'jun'
	JULIO = 'jul'
	AGOSTO = 'ago'
	SETIEMBRE = 'set'
	OCTUBRE = 'oct'
	NOVIEMBRE = 'nov'
	DICIEMBRE = 'dic'
	MONTHS_IN_YEAR_CHOICES = (
		(ENERO , 'enero'),
		(FEBRERO , 'febrero'),
		(MARZO , 'marzo'),
		(ABRIL , 'abril'),
		(MAYO , 'mayo'),
		(JUNIO , 'junio'),
		(JULIO , 'julio'),
		(AGOSTO , 'agosto'),
		(SETIEMBRE , 'setiembre'),
		(OCTUBRE , 'octubre'),
		(NOVIEMBRE , 'noviembre'),
		(DICIEMBRE , 'diciembre'),
	) 
	month_in_year = models.CharField (
			max_length=3,
			choices=MONTHS_IN_YEAR_CHOICES,
			default=ENERO	
		)

	def __str__ (self):
		return self.month_in_year 


class Days (models.Model):
	day_in_month = models.ForeignKey (Months, on_delete=models.CASCADE) 
	day = models.IntegerField (validators=[MinValueValidator(1), MaxValueValidator(31)])

	def __str__ (self):
		return self.day


from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def home (request): 
# 	return render (request,'tasks/home.html')

# def calendar (request): 
# 	return render (request,'tasks/calendar.html')

class HomeView (TemplateView):
	template_name = "tasks/home.html"


class TaskView (TemplateView):
	template_name = "tasks/tasks.html"

class CreateTask (TemplateView):
	template_name = "tasks/create.html"

class DayTask (TemplateView):
	template_name = "tasks/day.html"

	def retDay (self, day):
		if day < 30:
			return day

		else:
			return 'que mal fallo'


class MonthTask (TemplateView):
	template_name = "tasks/month.html"
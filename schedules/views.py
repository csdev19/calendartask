from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CalendarView (TemplateView):
    template_name = "schedules/calendar.html"


class DayView (TemplateView):
	template_name = "tasks/day.html"


class MonthView (TemplateView):
	template_name = "tasks/month.html"


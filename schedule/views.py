from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CalendarView (TemplateView):
    template_name = "schedule/calendar.html"

from django.urls import path

# from . import views
from schedules.views import DayView,  MonthView, CalendarView


urlpatterns = [
    # path('', views.home, name='home'),
    path ('', CalendarView.as_view()),
    # path ('create/', CreateTask.as_view()),
    path ('<str:month>/', MonthView.as_view()),
    path ('<str:month>/<int:day>/', DayView.as_view()),
    # path ('<str:month>/<int:day>/create/', CreateTask.as_view()),
]


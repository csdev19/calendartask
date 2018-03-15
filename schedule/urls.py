from django.urls import path

# from . import views
from schedule.views import CalendarView


urlpatterns = [
    # path('', views.home, name='home'),
    path ('', CalendarView.as_view()),
    # path ('create/', CreateTask.as_view()),
    # path ('create/<int:day>/', DayView.as_view()),
    # path ('<str:month>/', MonthView.as_view()),
]

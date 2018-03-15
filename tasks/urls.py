from django.urls import path

# from . import views
from tasks.views import TaskView, CreateTask, DayView,  MonthView


urlpatterns = [
    # path('', views.home, name='home'),
    path ('', TaskView.as_view()),
    path ('create/', CreateTask.as_view()),
    path ('create/<int:day>/', DayView.as_view()),
    path ('<str:month>/', MonthView.as_view()),
]

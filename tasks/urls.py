from django.urls import path

# from . import views
from tasks.views import TaskView, CreateTask, DayTask,  MonthTask


urlpatterns = [
    # path('', views.home, name='home'),
    path ('', TaskView.as_view()),
    # path ('create/', CreateTask.as_view()),
    path ('<str:month>/', MonthTask.as_view()),
    path ('<str:month>/<int:day>/', DayTask.as_view()),
    path ('<str:month>/<int:day>/create/', CreateTask.as_view()),
]

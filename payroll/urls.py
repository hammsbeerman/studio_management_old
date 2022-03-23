from django.urls import path
from . import views

urlpatterns = [
    path('timecard', views.timecard, name='timecard'),
]

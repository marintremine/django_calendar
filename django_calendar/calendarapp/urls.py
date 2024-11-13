from django.shortcuts import render
from django.urls import path

from calendarapp import views


# Create your views here.
urlpatterns = [
    path("", views.CalendarView.as_view(), name="calendar"),
]
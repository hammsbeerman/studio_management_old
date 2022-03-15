from django.shortcuts import render, redirect
from django.contrib import messages

def timecard(request):
    return render(request, 'payroll/timecard.html')

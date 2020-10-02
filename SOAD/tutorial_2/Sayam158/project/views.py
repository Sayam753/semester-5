from django.shortcuts import render, render
from .models import Student

# Create your views here.


def home(request):
    return render(request, 'index.html', dict(students=Student.objects.all()))

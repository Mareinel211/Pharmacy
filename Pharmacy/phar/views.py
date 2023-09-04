from django.shortcuts import render
from django.http import HttpResponse
from .models import Phar

def home(request):
    phar = Phar.objects.all()
    return render(request,'home.html',{'phar': phar})



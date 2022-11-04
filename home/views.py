from django.shortcuts import render
from .models import Slider


def home_list(request):
    slider = Slider.objects.all()
    return render(request, 'home/home_list.html', {'slider': slider})
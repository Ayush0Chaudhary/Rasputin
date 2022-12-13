from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Room

def home(request):
    return render(request, template_name='home.html')

def room(request, pk):
    room = Room.objects.get(id= pk)
    return render(request=request, template_name='room.html', context={"room":room})
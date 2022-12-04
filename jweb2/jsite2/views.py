from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Projects

def home(request):
    return render(request, 'jweb2/home.html')

def projects(request):
    pack = Projects.objects.all()
    return render(request, 'jweb2/projects.html', {'context':pack})
def aboutme(request):
    return render(request, 'jweb2/aboutme.html')
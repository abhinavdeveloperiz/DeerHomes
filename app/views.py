from django.shortcuts import render
from .models import gallery, Project
# Create your views here.

def home(request):
    image=gallery.objects.order_by('-id')[:8]
    context={
        'image':image
        }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    projects = Project.objects.order_by('-id')[:6]
    context = {
        'projects': projects
    }
    return render(request, 'services.html',context)

def management(request):
    return render(request, 'management.html')

def projects(request):
    projects = Project.objects.order_by('-id')
    context = {
        'projects': projects
    }
    return render(request, 'projects.html',context)

def contact(request):
    return render(request, 'contact.html')
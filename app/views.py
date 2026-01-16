from django.shortcuts import render,redirect,get_object_or_404
from .models import gallery, Project,BannerHome,ServiceCategory,Service
# Create your views here.

def home(request):
    image=gallery.objects.order_by('-id')[:8]
    banner=BannerHome.objects.last()
    services=ServiceCategory.objects.prefetch_related('services')
    projects=Project.objects.order_by('-id')[:6]
    context={
        'image':image,
        'banner':banner,
        'services':services,
        'projects':projects
        }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')

def services(request):
    projects = Project.objects.order_by('-id')[:6]
    service_categories = ServiceCategory.objects.prefetch_related('services')

    context = {
        'projects': projects,
        'service_categories': service_categories
    }
    return render(request, 'services.html',context)

def service_category_detail(request, category_id):
    category = get_object_or_404(ServiceCategory, id=category_id)
    services = Service.objects.filter(category=category)

    context = {
        'category': category,
        'services': services
    }
    return render(request, 'service_category_detail.html', context)

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)

    context = {
        'service': service
    }
    return render(request, 'service_detail.html', context)


def management(request):
    return render(request, 'management.html')

def projects(request):
    projects = Project.objects.order_by('-id')
    context = {
        'projects': projects
    }
    return render(request, 'projects.html',context)

def Project_details(request,pk):
    project=Project.objects.get(id=pk)
    context={
        'project':project
    }
    return render(request, 'project_details.html',context)


def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
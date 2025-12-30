from django.contrib import admin
from .models import gallery, Project,BannerHome, ServiceCategory,Service

# Register your models here.

admin.site.register(gallery)
admin.site.register(Project)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(BannerHome)
from django.contrib import admin
from .models import gallery, Project,BannerHome

# Register your models here.

admin.site.register(gallery)
admin.site.register(Project)
admin.site.register(BannerHome)
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    BannerHome, Project, ServiceCategory, Service,
    Blogs, TeamMember, Directors
)



def image_preview(image_field):
    if image_field:
        return format_html(
            '<img src="{}" style="height:60px;border-radius:6px;" />',
            image_field.url
        )
    return "-"



@admin.register(BannerHome)
class BannerHomeAdmin(admin.ModelAdmin):
    list_display = ("id", "preview1", "preview2")

    def preview1(self, obj):
        return image_preview(obj.image1)

    def preview2(self, obj):
        return image_preview(obj.image2)

    preview1.short_description = "Image 1"
    preview2.short_description = "Image 2"


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "image_preview")

    def image_preview(self, obj):
        return image_preview(obj.image)

    image_preview.short_description = "Preview"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "preview")
    list_filter = ("category",)
    search_fields = ("title", "category__name")
    readonly_fields = ("preview",)

    fieldsets = (
        ("Service Info", {
            "fields": ("category", "title", "description")
        }),
        ("Images", {
            "fields": (
                "image1", "image2", "image3",
                "image4", "image5", "preview"
            )
        }),
    )

    def preview(self, obj):
        images = [obj.image1, obj.image2, obj.image3, obj.image4, obj.image5]
        html = ""
        for img in images:
            if img:
                html += f'<img src="{img.url}" style="height:60px;margin:2px;border-radius:6px;" />'
        return format_html(html) if html else "-"




@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")
    search_fields = ("title",)

    def image_preview(self, obj):
        return image_preview(obj.image)

    image_preview.short_description = "Preview"




@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "photo_preview")

    def photo_preview(self, obj):
        return image_preview(obj.photo)

    photo_preview.short_description = "Photo"





@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    list_display = ("id", "photo_preview")

    def photo_preview(self, obj):
        return image_preview(obj.photo)

    photo_preview.short_description = "Photo"






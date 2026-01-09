from django.contrib import admin
from django.utils.html import format_html
from .models import (
    BannerHome,
    gallery,
    Project,
    ServiceCategory,
    Service
)

# -------------------------
# GLOBAL IMAGE PREVIEW MIXIN
# -------------------------
class ImagePreviewMixin:
    def image_preview(self, obj, field_name):
        image = getattr(obj, field_name, None)
        if image:
            return format_html(
                '<img src="{}" style="height:80px;border-radius:6px;object-fit:cover;" />',
                image.url
            )
        return "—"
    image_preview.short_description = "Preview"



class ImagePreviewbanner:
    def preview(self, image):
        if image:
            return format_html(
                '<img src="{}" style="height:80px;border-radius:6px;object-fit:cover;" />',
                image.url
            )
        return "—"


# -------------------------
# BANNER ADMIN (FIXED)
# -------------------------
@admin.register(BannerHome)
class BannerHomeAdmin(ImagePreviewbanner, admin.ModelAdmin):
    list_display = ('id', 'image1_preview', 'image2_preview')

    def image1_preview(self, obj):
        return self.preview(obj.image1)
    image1_preview.short_description = "Image 1"

    def image2_preview(self, obj):
        return self.preview(obj.image2)
    image2_preview.short_description = "Image 2"


# -------------------------
# GALLERY ADMIN
# -------------------------
@admin.register(gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    search_fields = ('title',)

    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="height:80px;border-radius:6px;" />',
            obj.image.url
        )


# -------------------------
# PROJECT ADMIN
# -------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'location', 'main_image_preview')
    list_filter = ('type',)
    search_fields = ('title', 'location', 'client_name')

    fieldsets = (
        ("Project Information", {
            "fields": ("title", "type", "client_name", "location", "description")
        }),
        ("Project Images", {
            "fields": ("image1", "image2", "image3", "image4", "image5")
        }),
    )

    def main_image_preview(self, obj):
        return format_html(
            '<img src="{}" style="height:60px;border-radius:4px;" />',
            obj.image1.url
        )
    main_image_preview.short_description = "Main Image"


# -------------------------
# SERVICE INLINE (CRITICAL)
# -------------------------
class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0
    show_change_link = True

    fields = (
        'title',
        'description',
        'image1', 'image1_preview',
        'image2', 'image2_preview',
        'image3', 'image3_preview',
        'image4', 'image4_preview',
        'image5', 'image5_preview',
    )

    readonly_fields = (
        'image1_preview',
        'image2_preview',
        'image3_preview',
        'image4_preview',
        'image5_preview',
    )

    def image1_preview(self, obj):
        return self._preview(obj, 'image1')

    def image2_preview(self, obj):
        return self._preview(obj, 'image2')

    def image3_preview(self, obj):
        return self._preview(obj, 'image3')

    def image4_preview(self, obj):
        return self._preview(obj, 'image4')

    def image5_preview(self, obj):
        return self._preview(obj, 'image5')

    def _preview(self, obj, field):
        image = getattr(obj, field, None)
        if image:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;object-fit:cover;" />',
                image.url
            )
        return "—"


# -------------------------
# SERVICE CATEGORY ADMIN
# -------------------------
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')
    search_fields = ('name',)
    inlines = [ServiceInline]

    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="height:60px;border-radius:6px;" />',
            obj.image.url
        )
    image_preview.short_description = "Category Image"


# -------------------------
# SERVICE ADMIN (STANDALONE)
# -------------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image1_preview')
    list_filter = ('category',)
    search_fields = ('title',)

    fieldsets = (
        ("Service Information", {
            "fields": ("category", "title", "description")
        }),
        ("Service Images", {
            "fields": (
                "image1", "image2", "image3", "image4", "image5"
            )
        }),
    )

    def image1_preview(self, obj):
        if obj.image1:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:4px;" />',
                obj.image1.url
            )
        return "—"
    image1_preview.short_description = "Preview"

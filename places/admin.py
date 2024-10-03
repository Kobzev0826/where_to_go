from django.contrib import admin

from places.models import Place, Image

# Register your models here.
# admin.site.register(Place)
# admin.site.register(Image)

class ImageInline(admin.TabularInline):
    model=Image
    readonly_fields = ['image_preview', ]

    def image_preview(self, obj):
        return obj.image_preview

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
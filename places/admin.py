from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model=Image
    readonly_fields = ['image_preview', ]

    def image_preview(self, obj):
        return obj.image_preview

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image
    raw_id_fields = ("place",)
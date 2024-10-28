from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places.views import show_place, show_start_page

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("place/<int:place_id>/", show_place, name="place-detail"),
        path("", show_start_page),
        path("tinymce/", include("tinymce.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)

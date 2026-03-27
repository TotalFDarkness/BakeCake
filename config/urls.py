from django.contrib import admin
from django.urls import path
from BakeCake import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.index, name="index"),
    path("lk/", views.lk, name="lk"),
    path("api/cake-data/", views.get_cake_data, name="cake-data"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""tiggolino URL Configuration

We will include an seperate documentation for this project, that you can access via google drive
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



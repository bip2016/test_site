from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('upload/',image_view, name='upload'),
    path('success/',success, name='success'),
    path('images/', display_images, name = 'images'),
]


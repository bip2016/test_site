from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','name','date','Img')

admin.site.register(Photo, PhotoAdmin)
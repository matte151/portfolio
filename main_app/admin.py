from django.contrib import admin

# Register your models here.

from .models import Page, Photo, Blurb

admin.site.register(Page)
admin.site.register(Photo)
admin.site.register(Blurb)

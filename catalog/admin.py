from django.contrib import admin
from catalog import models

# Register your models here.

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin) :
    list_filter = ['approved', 'tag', 'user']
    list_display = [field.name for field in models.Website._meta.fields]
    list_display.remove('id')
    list_editable = ['approved']

admin.site.register(models.UserProfile)
admin.site.register(models.Tag)

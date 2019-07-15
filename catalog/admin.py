from django.contrib import admin
from catalog import models


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin) :
    list_filter = ['approved', 'tag', 'user']
    list_display = [field.name for field in models.Website._meta.fields]
    list_display.remove('id')
    list_editable = ['approved']

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Tag)
admin.site.register(models.UserAndWebsite)

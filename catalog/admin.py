from django.contrib import admin
from catalog import models


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin) :
    list_filter = ('tag', 'user')
    list_display = [field.name for field in models.Website._meta.fields]

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Tag)
admin.site.register(models.UserAndWebsite)

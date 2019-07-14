from django.contrib import admin
from catalog import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Tag)
admin.site.register(models.Website)
admin.site.register(models.UserAndWebsite)

from django.contrib import admin
from backend import models

admin.site.register(models.Item)
admin.site.register(models.Comment)
admin.site.register(models.Category)
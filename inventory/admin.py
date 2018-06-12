from django.contrib import admin

from . import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    pass

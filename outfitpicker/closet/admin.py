from django.contrib import admin
from closet.models import (
    Closet,
    ClothingItem,
)

# Register your models here.


@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Closet)
class ClosetAdmin(admin.ModelAdmin):
    pass

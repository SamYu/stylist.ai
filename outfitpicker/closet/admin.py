from django.contrib import admin
from closet.models import (
    Closet,
    ClothingItem,
    Outfit,
)
# Register your models here.

class ClothingItemInline(admin.TabularInline):
    model = ClothingItem

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Closet)
class ClosetAdmin(admin.ModelAdmin):
    inlines = [ClothingItemInline,]

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    pass
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class ClothingItem(models.Model):
    clothing_type_choices = (
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('shoe', 'Shoe'),
        ('accessory', 'Accessory'),
        ('outerwear', 'Outerwear'),
    )
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    clothing_type = models.CharField(
        choices=clothing_type_choices,
        max_length=100,
    )

class Closet(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="closet"
    )
    clothes = models.ForeignKey(
        ClothingItem,
        on_delete=models.CASCADE,
        related_name="closet"
    )
    count = models.IntegerField()

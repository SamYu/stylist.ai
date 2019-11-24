from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Closet(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="closet"
    )
    count = models.IntegerField()

    def __str__(self):
        return self.user.email + '\'s closet'


class ClothingMaterial(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
       return self.name

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
    closet = models.ForeignKey(
        Closet,
        on_delete=models.CASCADE,
        related_name="clothes",
        null=True,
        blank=True,
    )
    material = models.ForeignKey(
        ClothingMaterial,
        on_delete=models.CASCADE,
        related_name="clothes",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Outfit(models.Model):
    name = models.CharField(max_length=100)
    clothes = models.ManyToManyField(
        ClothingItem,
        related_name="outfits"
    )
    closet = models.ForeignKey(
        Closet,
        on_delete=models.CASCADE,
        related_name="outfits",
        null=True,
        blank=True,
    )
    rating = models.IntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
       return self.name

from django.db import models

class ClothingItem(models.model):
    clothing_type_choices = (
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('shoe', 'Shoe'),
        ('accessory', 'Accessory'),
        ('outerwear', 'Outerwear'),
    )
    name = models.CharField(max_length=100)
    colour = models.CharField()
    material = models.CharField()
    clothing_type = models.CharField(
        choices=clothing_type_choices,
    )

class Closet(models.model):
    clothes = ClothingItem()
    count = models.IntegerField()

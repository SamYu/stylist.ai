from django.core.management.base import BaseCommand, CommandError
from closet.models import (
    Outfit,
    ClothingItem,
    Closet,
    ClothingMaterial
)
import webcolors
import random

def closest_colour(rgbColor):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgbColor[0]) ** 2
        gd = (g_c - rgbColor[1]) ** 2
        bd = (b_c - rgbColor[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(rgbColor):
    try:
        colorName = webcolors.rgb_to_name(rgbColor)
    except ValueError:
        colorName = closest_colour(rgbColor)
    return colorName

def generate_n_clothes(closet_id, n):
    try:
        closet = Closet.objects.get(id=closet_id)
    except:
        raise 'Closet does not exist'
    for i in range(n):
        random_rgb = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        new_color = get_colour_name(random_rgb)
        materials = ['wool', 'cotton', 'satin', 'denim', 'leather', 'suede', 'silk', 'cashmere', 'canvas',
            'polyester', 'gold', 'silver', 'gold', 'steel',
        ]
        random_material = random.choice(materials)
        new_material = ClothingMaterial(
            name=random_material,
        )
        new_material.save()
        new_type = ClothingItem.clothing_type_choices[random.randint(0, 4)][0]
        new_name = new_color + " " + new_type + " " + str(i)
        new_clothing = ClothingItem(
            name=new_name,
            colour=new_color,
            material=new_material,
            clothing_type=new_type,
            closet=closet,
        )
        new_clothing.save()

class Command(BaseCommand):
    help = 'Generates n clothing items'

    def add_arguments(self, parser):
        parser.add_argument('closet_id', type=int)
        parser.add_argument('num', type=int)

    def handle(self, *args, **options):
        num = options['num']
        closet_id = options['closet_id']
        generate_n_clothes(closet_id, num)

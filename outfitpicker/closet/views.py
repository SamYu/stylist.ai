from django.shortcuts import render

from django.http import HttpResponse

from closet.models import (
    Outfit,
    ClothingItem,
    Closet
)

import webcolors
import random


def index(request):
    return HttpResponse("hack western baby")

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

def generate_n_clothes(seed, n):
    for i in range(n):
        random.seed(seed)
        clothing_type_choice = (
            ('top', 'Top'),
            ('bottom', 'Bottom'),
            ('shoe', 'Shoe'),
            ('accessory', 'Accessory'),
            ('outerwear', 'Outerwear'),
        )
        random_rgb = (
            random.randInt(0, 255),
            random.randInt(0, 255),
            random.randint(0, 255)
        )
        new_color = get_colour_name(random_rgb)
        #new_material = 
        new_type = clothing_type_choice[random.randInt(0, 4)][0]
        new_name = new_color + " " + new_type + " " + i





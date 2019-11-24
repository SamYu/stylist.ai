from django.core.management.base import BaseCommand, CommandError
from closet.models import (
    Outfit,
    ClothingItem,
    Closet,
    ClothingMaterial
)
import random

def get_random_clothes_list():
    clothes_list = []
    for clothing_type in ClothingItem.clothing_type_choices:
        clothes = ClothingItem.objects.all().filter(clothing_type=clothing_type[0])
        selected_clothing = random.choice(clothes)
        if (clothing_type == 'outerwear'):
            if (random.choice([0, 1]) == 1):
                clothes_list.append(selected_clothing)
        else:
            clothes_list.append(selected_clothing)
    return clothes_list
        

def generate_n_outfits(closet_id, num):
    try:
        closet = Closet.objects.get(id=closet_id)
    except:
        raise 'Closet does not exist'
    for i in range(num):
        new_name = 'Outfit ' + str(i)
        new_clothes = get_random_clothes_list()
        new_rating = random.randint(1, 10)
        new_outfit = Outfit(
            name=new_name,
            rating=new_rating,
            closet=closet
        )
        new_outfit.save()
        new_outfit.clothes.add(*new_clothes)
        new_outfit.save()


class Command(BaseCommand):
    help = 'Generates n random outfits'

    def add_arguments(self, parser):
        parser.add_argument('closet_id', type=int)
        parser.add_argument('num', type=int)

    def handle(self, *args, **options):
        closet_id = options['closet_id']
        num = options['num']
        generate_n_outfits(closet_id, num)


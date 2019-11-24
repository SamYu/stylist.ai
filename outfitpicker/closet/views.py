import json
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from random import randint
from django.core import serializers
from closet.models import (
    ClothingItem,
    Closet,
    ClothingMaterial,
    Outfit,
)
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def add_clothing_item(request):
    user = request.user
    closet = user.closet
    json_data = json.loads(request.body)
    #import ipdb; ipdb.set_trace()

    new_clothing = ClothingItem(
        name=json_data['name'],
        clothing_type=json_data['clothing_type'],
        colour=json_data['colour'],
        closet=closet
    )
    new_clothing.save()
    return JsonResponse({'status_code': 200})

@csrf_exempt
def remove_clothing_item(request):
    json_data = json.loads(request.body)
    id = json_data['id']
    user = request.user
    closet = user.closet
    clothing_item = closet.clothes.all().get(id=id)
    clothing_item.delete()
    response.status_code = 200
    return response

@csrf_exempt
def view_clothes(request):
    clothesDict = []
    user = request.user
    closet = user.closet
    clothes_set = closet.clothes.all()
    for index, item in enumerate(clothes_set):
        itemInfo = {
            "id": item.id,
            "name": item.name,
            "clothing_type": item.clothing_type,
            "colour": item.colour,
            "material": item.material.name,
            }
        clothesDict.append(itemInfo)
    # import ipdb; ipdb.set_trace()
    return HttpResponse(json.dumps(clothesDict), content_type="application/json")

@csrf_exempt
def view_clothing_item(request):
    user = request.user
    closet = user.closet
    json_data = json.loads(request.body)
    id = json_data['id']
    clothing_item = closet.clothes.get(id=id)
    serialized_obj = serializers.serialize('json', [clothing_item])
    return HttpResponse(serialized_obj, content_type="application/json")


@csrf_exempt
def view_outfit(request):
    user = request.user
    closet = user.closet
    json_data = json.loads(request.body)
    id = json_data['id']
    outfit_item = closet.outfits.get(id=id)
    serialized_obj = serializers.serialize('json', [outfit_item])
    return HttpResponse(serialized_obj, content_type="application/json")

@csrf_exempt
def suggested_outfit(request):
    user = request.user
    closet = user.closet
    outfit_set = closet.outfits.all()
    outfit_count = outfit_set.count()
    randomOutfit = outfit_set[randint(0, outfit_count - 1)]
    serialized_obj = serializers.serialize('json', [randomOutfit])
    return HttpResponse(serialized_obj, content_type="application/json")

@csrf_exempt
def add_outfit(request):
    user = request.user
    clothArray = []
    closet = user.closet
    json_data = json.loads(request.body)
    for item in range(len(json_data.clothItem)):
        id = item.id
        clothingItem = closet.clothes.get(id=id)
        clothArray.append(clothingItem)
    new_outfit = Outfit(
        name=json_data.name,
        rating=json_data.rating,
    )
    new_outfit.save()
    new_outfit.clothes.add(*clothArray)
    new_outfit.save()
    response = HttpResponse()
    response.status_code = 200
    return response


@csrf_exempt
def remove_outfit(request):
    user = request.user
    closet = user.closet
    json_data = json.loads(request.body)
    id = json_data['id']
    removed_outfit = closet.outfits.all().get(id=id)
    removed_outfit.delete()
    response = HttpResponse()
    response.status_code = 200
    return response

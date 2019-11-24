import json
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from closet.models import (
    ClothingItem,
    Closet,
    ClothingMaterial,
)
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_clothing_item(request):
    user = request.user
    closet = user.closet
    json_data = json.loads(request.body)
    #import ipdb; ipdb.set_trace()
    material = json_data['material']
    try:
        clothing_material = ClothingMaterial.get(name=material)
    except:
        clothing_material = ClothingMaterial(name=material)
        clothing_material.save()

    new_clothing = ClothingItem(
        name=json_data['name'],
        clothing_type=json_data['clothing_type'],
        material=clothing_material,
        colour=json_data['colour'],
        closet=closet
    )
    new_clothing.save()
    response = HttpResponse()
    response.status_code = 200
    return response

@csrf_exempt
def remove_clothing_item(request):
    json_data = json.loads(request.body)
    id = json_data['id']
    user = request.user
    closet = user.closet
    clothing_item = closet.clothes.all().get(id=id)
    clothing_item.delete()
    rresponse.status_code = 200
    return response

@csrf_exempt
def view_clothes(request):
    clothesDict = {}
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
        clothesDict[str(index)] = itemInfo
    # import ipdb; ipdb.set_trace()
    return HttpResponse(json.dumps(clothesDict), content_type="application/json")


import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from closet.models import (
    ClothingItem,
    Closet,
)
from django.views.decorators.csrf import csrf_exempt



class ClothingItemView(APIView):

    @csrf_exempt
    def add_clothing_item(request):
        user = request.user
        closet = user.closet
        json_data = json.loads(request.body)
        # import ipdb; ipdb.set_trace()
        new_clothing = ClothingItem(
        name=json_data['name'],
        clothing_type=json_data['clothing_type'],
        material=json_data['material'],
        colour=json_data['colour'],
        closet=closet
        )
        new_clothing.save()
        return(new_clothing.id)
           
        
     

        # def remove_clothing_item(request):
        # id = request
        # clothing_item = ClothingItem.objects.get(
        #     id=id,
        # )
        # clothing_item.delete()

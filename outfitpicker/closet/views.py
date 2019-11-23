from django.shortcuts import render

from django.http import HttpResponse
from closet.models import (
    ClothingItem,
    Closet,
)

def index(request):
    return HttpResponse("hack western baby")


def add_clothing_item(request):
    user = get_auth_user()
    closet = user.closet
    new_clothing = ClothingItem(
        name=request.data.get('name'),
        type=request.data.get('type'),
        material=request.data.get('material'),
        colour=request.data.get('colour'),
        closet=closet
    )

# name: 'nike shirt'
# type: 'Top'
# colour: 'Red'


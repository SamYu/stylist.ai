from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from closet.models import Closet
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def register(request):
    # username
    # email
    # password
    json_data = json.loads(request.body)
    username = json_data["username"]
    email = json_data["email"]
    password = json_data["password"]
    new_user = User.objects.create_user(
        username=username, email=email, password=password)
    new_user.save()

    new_closet = Closet(user=new_user, count=0)
    new_closet.save()
    return HttpResponse("hack western baby")


@csrf_exempt
def login(request):
    # username
    # password
    json_data = json.loads(request.body)
    username = json_data["username"]
    password = json_data["password"]

    user = authenticate(username=username, password=password)

    response = HttpResponse()
    if user is not None:
        response.status_code = 200
        return response
    else:
        response.status_code = 401
        return response

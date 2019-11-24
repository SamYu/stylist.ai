from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from closet.models import Closet
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def register(request):
    # username
    # email
    # password
    try:
        json_data = json.loads(request.body)
        username = json_data["username"]
        email = json_data["email"]
        password = json_data["password"]
        new_user = User.objects.create_user(
            username=username, email=email, password=password)
        new_user.save()

<<<<<<< HEAD
        new_closet = Closet(user=new_user, count=0)
        new_closet.save()
        response = HttpResponse()
        response.status_code = 200
        return response
    except:
        response = HttpResponse()
        response.status_code = 320
        return response
=======
    new_closet = Closet(user=new_user, count=0)
    new_closet.save()
    return JsonResponse({'status_code': 200, 'message': 'success'})
>>>>>>> origin/master


@csrf_exempt
def loginUser(request):
    # username
    # password
    json_data = json.loads(request.body)
    username = json_data["username"]
    password = json_data["password"]

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'status_code': 200})
    else:
        return JsonResponse({'status_code': 401})


@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({'status_code': 200})

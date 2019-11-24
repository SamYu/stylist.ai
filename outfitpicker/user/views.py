from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from closet.models import Closet


def register(request):
    # username
    # email
    # password
    username = request.body.username
    email = request.body.email
    password = request.body.password
    new_user = User.objects.create_user(
        username=username, email=email, password=password)

    new_closet = Closet(user=new_user, count=0)
    new_closet.save()
    return HttpResponse("hack western baby")


def login(request):
    # username
    # password
    return

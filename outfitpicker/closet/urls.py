from django.urls import path
from . import views

urlpatterns = [
    path('add_clothes', views.add_clothing_item, name='add_clothes'),
]
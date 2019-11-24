from django.urls import path
from . import views

urlpatterns = [
    path('clothing', views.ClothingItemView, name='clothing'),
    path('add_clothing_item', views.ClothingItemView.add_clothing_item, name="add_clothes")
]
from django.urls import path
from . import views

urlpatterns = [
    path('add_clothing_item', views.add_clothing_item, name="add_clothes"),
    path('remove_clothing_item', views.remove_clothing_item, name="remove_clothes"),
    path('view_clothes', views.view_clothes, name="view_clothes")
]
from django.urls import path
from . import views

urlpatterns = [
    path('add_clothing_item', views.add_clothing_item, name="add_clothes"),
    path('remove_clothing_item', views.remove_clothing_item, name="remove_clothes"),
    path('view_clothes', views.view_clothes, name="view_clothes"),
    path('suggested_outfit', views.suggested_outfit, name="suggested_outfit"),
    path('add_outfit', views.add_outfit, name="add_outfit"),
    path('remove_outfit', views.remove_outfit, name="remove_outfit"),
    path('view_outfit', views.view_outfit, name="view_outfit"),
    path('view_clothing_item', views.view_clothing_item, name="view_clothing_item"),
]
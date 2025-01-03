from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_app, name="home_app"),
    path("menu/", views.menu, name="menu"),
    path("menu/<int:item_id>/", views.item_detail, name="item_detail"),
    path("search_items/", views.menu_items_view, name="menu_items_view"),
]

from django.urls import path, include
from . import views
app_name = "chinese"
urlpatterns = [
    path("add_food/", views.add_food, name='add_food'),
    path("food_detail/<int:pk>/", views.food_detail, name='food_detail'),
    path("food_delete/<int:pk>/", views.food_delete, name='food_delete'),
    path("modify_cart/", views.modify_cart, name='modify_cart'),
]

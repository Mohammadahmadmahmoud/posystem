from django.urls import path
from . import views

urlpatterns = [
   path('create-shop/', views.create_shop, name="create_shop"),
   path('index/', views.index, name="index"),
   path('shop/<str:store_id>/add-item/', views.add_item, name="add_item"),

]
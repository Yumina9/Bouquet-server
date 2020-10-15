from django.urls import path
from shops import views

urlpatterns = [
    path('shops/', views.shop_list),
    path('shop/<int:pk>/', views.shop_detail),
    path('shop/<int:pk>/flowers', views.shop_flowers_list),
    path('shop/<int:pk>/bouquets', views.shop_bouquets_list),
    path('shop/<int:shops_id>/flowers/<int:id>',views.shop_flower_detail),
    path('shop/<int:shops_id>/bouquets/<int:id>',views.shop_bouquet_detail),
]
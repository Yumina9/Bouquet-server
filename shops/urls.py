from django.urls import path
from shops import views

urlpatterns = [
    path('shops/', views.shop_list),
    path('shop/<int:pk>/', views.shop_detail),
    path('shop/<int:pk>/flowers', views.shop_detail_flowers),
    path('shop/<int:pk>/bouquets', views.shop_detail_bouquets),
    path('shop/<int:shop_id>/flowers/<int:flower_id>',views.shop_flower_detail),
    path('shop/<int:shop_id>/bouquets/<int:bouquet_id>',views.shop_bouquet_detail),
]
from django.urls import path
from shops import views

urlpatterns = [
    path('shops/', views.shop_list),
    path('shop/<int:pk>/', views.shop_detail),
    path('shop/<int:pk>/flowers', views.shop_detail_flowers),
    path('shop/<int:pk>/bouquets', views.shop_detail_bouquets)
]
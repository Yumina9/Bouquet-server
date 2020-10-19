from django.urls import path
from shops import views

urlpatterns = [
    path('shops/', views.shop_list),
    path('shop/<int:pk>/', views.shop_detail),
    path('shop/<int:pk>/flowers', views.shop_flowers_list),
    path('shop/<int:pk>/bouquets', views.shop_bouquets_list),
    path('shop/<int:pk>/ribbons', views.shop_ribbons_list),
    path('shop/<int:pk>/wrappingPapers', views.shop_wrappingPaper_list),
    path('shop/<int:shops_id>/flower/<int:id>',views.shop_flower_detail),
    path('shop/<int:shops_id>/bouquet/<int:id>',views.shop_bouquet_detail),
]
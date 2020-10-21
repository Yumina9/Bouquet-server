from django.urls import path
from shops import views

urlpatterns = [
    path('list', views.shop_list),
    path('<int:pk>/', views.shop_detail),
    path('<int:pk>/flowers', views.shop_flowers_list),
    path('<int:pk>/bouquets', views.shop_bouquets_list),
    path('<int:pk>/ribbons', views.shop_ribbons_list),
    path('<int:pk>/wrappingPapers', views.shop_wrappingPaper_list),
    path('<int:shops_id>/flower/<int:id>',views.shop_flower_detail),
    path('<int:shops_id>/bouquet/<int:id>',views.shop_bouquet_detail),
    path('my', views.MyShop.as_view())
]
from django.urls import path
from shops import views

urlpatterns = [
    path('shops/', views.shop_list),
    path('shops/<int:pk>/', views.shop_detail)
]
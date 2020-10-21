from django.urls import path
from bouquet_order import views

urlpatterns = [
    path('', views.bouquet_order_list.as_view()),
    path('<int:pk>/', views.bouquet_order_detail.as_view()),
    path('orderlist', views.ShopOrderList.as_view()),
]
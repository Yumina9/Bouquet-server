from django.urls import path
from bouquets import views

urlpatterns =[
    path('bouquets/', views.bouquet_list),
    path('bouquets/<int:pk>/', views.bouquet_detail),
]
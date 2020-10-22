from django.urls import path
from bouquets import views

urlpatterns =[
    path('', views.bouquet_list),
    path('<int:pk>/', views.bouquet_detail),
]
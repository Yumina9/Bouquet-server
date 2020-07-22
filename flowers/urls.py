from django.urls import path
from flowers import views

urlpatterns = [
    path('flowers/', views.flower_list),
    path('flowers/<int:pk>/', views.flower_detail),
]
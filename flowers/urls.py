from django.urls import path
from flowers import views

urlpatterns = [
    path('', views.flower_list),
    path('<int:pk>/', views.flower_detail),
]
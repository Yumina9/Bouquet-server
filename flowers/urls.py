from django.urls import path
from flowers import views

urlpatterns = [
    path('', views.flower_list),
    path('flower/', views.FlowerList.as_view()),
    path('flower/<int:pk>/', views.FlowerDetail.as_view()),
    path('<int:pk>/', views.flower_detail),
]
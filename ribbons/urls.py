from django.urls import path
from ribbons import views

urlpatterns = [
    path('', views.ribbon_list),
    path('<int:pk>/', views.ribbon_detail),
]
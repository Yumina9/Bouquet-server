from django.urls import path
from wrappingPapers import views

urlpatterns = [
    path('', views.wrappingPaper_list),
    path('<int:pk>/', views.wrappingPaper_detail),
]
from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, UserViewSet
from rest_framework.routers import DefaultRouter
from users import views
app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('me/', views.UserView.as_view()),
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    # path('users/', UserViewSet.as_view()),
]

urlpatterns += router.urls

from django.urls import path

from .views import RegisterAPIView, activate

from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<str:activation_code>/', activate)

]
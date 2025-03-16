from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from User.views import UserTokenObtainView

urlpatterns = [
    path('token/', UserTokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
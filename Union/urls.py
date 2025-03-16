from django.urls import path
from .views import DashboardView, MembersView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import UnionTokenObtainView

urlpatterns = [
    path('dashboard/', DashboardView.as_view()),
    path('members/', MembersView.as_view()),
    path('token/', UnionTokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
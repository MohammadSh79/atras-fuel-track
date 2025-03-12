from django.urls import path
from .views import DashboardView, MembersView

urlpatterns = [
    path('dashboard/', DashboardView.as_view()),
    path('members/', MembersView.as_view()),
]
# leads/api/urls.py
from django.urls import path
from .views import LeadListAPIView, LeadDetailAPIView

urlpatterns = [
    path('leads/', LeadListAPIView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailAPIView.as_view(), name='lead-detail'),
]

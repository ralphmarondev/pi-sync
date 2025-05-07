from django.urls import path
from .views import FingerprintListView, FingerprintEnrollView, FingerprintDetailView

urlpatterns = [
    path('fingerprint/', FingerprintListView.as_view(), name='fingerprint-list'),
    path('fingerprint/enroll/', FingerprintEnrollView.as_view(), name='fingerprint-enroll'),
    path('fingerprint/details/<str:name>/', FingerprintDetailView.as_view(), name='fingerprint-detail'),
]

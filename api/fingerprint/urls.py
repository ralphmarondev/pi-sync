from django.urls import path
from .views import *

urlpatterns = [
    path('fingerprint/', FingerprintListView.as_view(), name='fingerprint-list'),
    path('fingerprint/enroll/', FingerprintEnrollView.as_view(), name='fingerprint-enroll'),
    path('fingerprint/details/<str:name>/', FingerprintDetailView.as_view(), name='fingerprint-detail'),
    path('fingerprint/assign/<str:name>/', FingerprintAssignView.as_view(), name='fingerprint-assign'),
    path('fingerprint/unassign/<str:name>/', FingerprintUnassignView.as_view(), name='fingerprint-unassign')
]

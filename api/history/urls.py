from django.urls import path

from .views import HistoryView

urlpatterns = [
    path('history/', HistoryView.as_view(), name='history_list'),
    path('history/<int:pk>/', HistoryView.as_view(), name='history_detail')
]

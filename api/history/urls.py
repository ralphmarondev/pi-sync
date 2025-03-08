from django.urls import path

from .views import HistoryView, RoomHistoryView, UserHistoryView

urlpatterns = [
    path('history/', HistoryView.as_view(), name='history_list'),
    path('history/<int:pk>/', HistoryView.as_view(), name='history_detail'),
    path('history/room/<int:room_id>/', RoomHistoryView.as_view(), name='history_room'),
    path('history/user/<str:username>/', UserHistoryView.as_view(), name='history_user')
]

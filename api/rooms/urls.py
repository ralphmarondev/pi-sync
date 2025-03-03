from django.urls import path

from .views import DoorView, OpenDoorView, CloseDoorView, DoorStatusView

urlpatterns = [
    path('doors/', DoorView.as_view(), name='door_list'),
    path('door/<int:pk>/', DoorView.as_view(), name='door_detail'),
    path('door/open/<int:pk>/', OpenDoorView.as_view(), name='door_open'),
    path('door/close/<int:pk>/', CloseDoorView.as_view(), name='door_close'),
    path('door/status/<int:pk>/', DoorStatusView.as_view(), name='door_status')
]

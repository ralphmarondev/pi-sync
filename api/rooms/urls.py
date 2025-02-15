from django.urls import path

from .views import DoorView, OpenDoorView, CloseDoorView

urlpatterns = [
    path('doors/', DoorView.as_view(), name='door_list'),
    path('door/<int:pk>/', DoorView.as_view(), name='door_detail'),
    path('door/<int:pk>/open/', OpenDoorView.as_view(), name='door_open'),
    path('door/<int:pk>/close/', CloseDoorView.as_view(), name='door_close'),
]

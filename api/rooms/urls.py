from django.urls import path

from .views import *

urlpatterns = [
    path('doors/', DoorListView.as_view(), name='door_list'),
    path('door/<int:pk>/', DoorDetailView.as_view(), name='door_detail'),
    path('door/new/', NewDoorView.as_view(), name='new-door'),
    path('door/update/<int:pk>/', UpdateDoorView.as_view(), name='update-door'),
    path('door/delete/<int:pk>/', DeleteDoorView.as_view(), name='delete-door'),
    path('door/open/<int:pk>/', OpenDoorView.as_view(), name='door_open'),
    path('door/close/<int:pk>/', CloseDoorView.as_view(), name='door_close'),
    path('door/status/<int:pk>/', DoorStatusView.as_view(), name='door_status'),
    path('doors/username/<str:username>/', RegisteredDoorsByUsernameView.as_view(), name='door_list_by_username'),

    # updates for desktop lol
    path('door/name/<str:name>/', GetDoorDetailByNameView.as_view(), name='door_detail_by_name'),
]

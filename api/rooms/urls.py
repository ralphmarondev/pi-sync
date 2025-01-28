from django.urls import path

from .views import DoorView
urlpatterns = [
	path('doors/', DoorView.as_view(), name='door_list'),
	path('door/<int:pk>/', DoorView.as_view(), name='door_detail')
]

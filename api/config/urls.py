from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('rooms.urls')),
    path('api/', include('history.urls')),
]

from django.urls import path

from .views import *

urlpatterns = [
    path('person/', TestPersonView.as_view()),
    path('person/<int:pk>/', TestPersonView.as_view())
]

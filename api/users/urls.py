from django.urls import path

from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('users/', UserListView.as_view(), name='users_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('user/username/<str:username>/', UserDetailByUsernameView.as_view(), name='user_detail_by_username'),
    path('user/password-hint/<str:username>/', UserPasswordHintView.as_view(), name='user_password_hint')
]

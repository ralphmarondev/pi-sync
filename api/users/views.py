from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

class UserRegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(data['password'])
            user.save()

            registered_doors = data.get('registered_doors', [])
            if registered_doors:
                user.registered_doors.set(registered_doors)

            return Response(data={
                'success': True,
                'message': 'User registered successfully',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(data={
            'success': False,
            'message': 'Registration failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username, is_deleted=False)
        except User.DoesNotExist:
            return Response(data={
                'success': False,
                'message': 'User not found or deleted'
            }, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            return Response(data={
                'success': True,
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        return Response(data={
            'success': False,
            'message': 'Invalid password'
        }, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.filter(is_deleted=False)
        serializer = UserSerializer(users, many=True)

        return Response(
            data={
                'success': True,
                'message': 'Users retrieved successfully',
                'users': serializer.data
            },
            status=status.HTTP_200_OK
        )

class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk, is_deleted=False)
        except User.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user)
        return Response(
            data={
                'success': True,
                'message': serializer.data
            },
            status=status.HTTP_200_OK
        )

class UserUpdateView(APIView):
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except  User.DoesNotExists:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(data.get('password', user.password))
            user.save()

            registered_doors = data.get('registered_doors', [])
            if registered_doors:
                user.registered_doors.set(registered_doors)
            return Response(
                data={
                    'success': True,
                    'message': 'User updated successfully'
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'success': False,
                'message': 'Update failed',
                'errors': serializer.errors
            }
        )

class UserDeleteView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        user.is_deleted = True
        user.save()

        return Response(
            data={
                'success': True,
                'message': 'User deleted successfully'
            },
            status=status.HTTP_200_OK
        )

class UserDetailByUsernameView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username, is_deleted=False)
        except User.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user)
        return Response(
            data={
                'success': True,
                'message': 'User retrieved successfully',
                'user': serializer.data
            },
            status=status.HTTP_200_OK
        )

class UserPasswordHintView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username, is_deleted=False)
        except User.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            data={
                'success': True,
                'message': 'Password hint retrieved successfully',
                'password_hint': user.hint_password
            },
            status=status.HTTP_200_OK
        )

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
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.models import FamilyMember
from authentication.serializers import FamilyMemberSerializer


class RegisterView(generics.CreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
    permission_classes = (AllowAny,)


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        family_member = authenticate(username=username, password=password)

        if family_member:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

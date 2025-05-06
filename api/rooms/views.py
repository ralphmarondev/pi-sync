from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from history.models import History
from rooms.serializers import DoorSerializer
from .models import Door
from users.models import User

class NewDoorView(APIView):
    def post(self, request):
        data = request.data
        serializer = DoorSerializer(data=data)
        if serializer.is_valid():
            door = serializer.save()
            door.save()
            return Response(
                data={
                    'success': True,
                    'message': 'Door created successfully',
                    'door': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                'success': False,
                'message': 'Door creation failed',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class DoorDetailView(APIView):
    def get(self, request, pk=None):
        try:
            door = Door.objects.get(pk=pk, is_deleted=False)
            serializer = DoorSerializer(door)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Door.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': 'Door not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

class DoorListView(APIView):
    def get(self, request):
        doors = Door.objects.filter(is_deleted=False)

        if not doors:
            return Response(
                data={
                    'success': False,
                    'message': 'No doors found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DoorSerializer(doors, many=True)
        return Response(
            data=serializer.data,
            status=HTTP_200_OK
        )

class UpdateDoorView(APIView):
    def put(self, request, pk):
        try:
            door = Door.objects.get(pk=pk, is_deleted=False)
        except Door.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': 'Door not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DoorSerializer(door, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'success': True,
                    'message': 'Door updated successfully',
                    'door': serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'success': False,
                'message': 'Door update failed',
                'errors': serializer.errors
            }
        )

class DeleteDoorView(APIView):
    def put(self, request, pk):
        try:
            door = Door.objects.get(pk=pk, is_deleted=False)
        except Door.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': 'Door not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        door.is_deleted = True
        door.save()
        return Response(
            data={
                'success': True,
                'message': 'Door deleted successfully'
            },
            status=status.HTTP_200_OK
        )

class OpenDoorView(APIView):
    def post(self, request, pk):
        door = get_object_or_404(Door, pk=pk, is_deleted=False)
        if not door.is_open:
            door.is_open = True
            door.save(update_fields=['is_open'])

        # NOTE: log action to history
        description = request.data.get('description', 'Opened via unknown')
        username = request.data.get('username', 'Unknown')
        history_entry = History(
            room=door,
            username=username,
            description=description
        )
        history_entry.save()

        return Response(
            data={
                'success': True,
                'message': 'Door opened',
                'is_open': door.is_open
            },
            status=status.HTTP_200_OK
        )

class CloseDoorView(APIView):
    def post(self, request, pk):
        door = get_object_or_404(Door, pk=pk, is_deleted=False)
        if door.is_open:
            door.is_open = False
            door.save(update_fields=['is_open'])

        # NOTE: log action to history
        description = request.data.get('description', 'Closed via unknown')
        username = request.data.get('username', 'Unknown')
        history_entry = History(
            room=door,
            username=username,
            description=description
        )
        history_entry.save()

        return Response(
            data={
                'success': True,
                'message': 'Door closed',
                'is_open': door.is_open
            },
            status=status.HTTP_200_OK
        )

class DoorStatusView(APIView):
    def get(self, request, pk):
        door = get_object_or_404(Door, pk=pk, is_deleted=False)
        return Response(
            data={
                'success': True,
                'message': 'Door status retrieved successfully',
                'is_open': door.is_open
            },
            status=HTTP_200_OK
        )

class RegisteredDoorsByUsernameView(APIView):
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

        doors = user.registered_doors.filter(is_deleted=False)  # assuming Door has is_deleted
        serializer = DoorSerializer(doors, many=True)

        return Response(
            data={
                'success': True,
                'message': f'Registered doors for {username} retrieved successfully',
                'doors': serializer.data
            },
            status=status.HTTP_200_OK
        )

# this is needed on desktop lol
class GetDoorDetailByNameView(APIView):
    def get(self, request, name):
        try:
            # door = Door.objects.get(name=name, is_deleted=False)
            # to ignore case sensitivity 
            door = Door.objects.get(name__iexact=name, is_deleted=False)
            serializer = DoorSerializer(door)
            return Response(
                data = {
                    'success': True,
                    'message': f'Door with name {name} retrieved successfully',
                    'door': serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Door.DoesNotExist:
            return Response(
                data={
                    'success': False,
                    'message': f'Door with name {name} not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
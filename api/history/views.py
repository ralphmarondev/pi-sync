from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from history.models import History
from history.serializers import HistorySerializer

class HistoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                history = History.objects.get(pk=pk)
                serializer = HistorySerializer(history)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except History.DoesNotExist:
                return Response(
                    data={
                        'message': 'History not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

        histories = History.objects.all().order_by('-timestamp')
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        try:
            room = Door.objects.get(id=data.get('room'))
        except Door.DoesNotExist:
            return Reponse(
                data={
                    'message': 'Invalid room ID'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = HistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'message': 'History entry created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomHistoryView(APIView):
    def get(self, request, room_id):
        histories = History.objects.filter(room_id=room_id).order_by('-timestamp')
        serializer = HistorySerializer(histories, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class UserHistoryView(APIView):
    def get(self, request, username):
        histories = History.objects.filter(username=username).order_by('-timestamp')

        if not histories.exists():
            return Response({'message': 'No history found for this username'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

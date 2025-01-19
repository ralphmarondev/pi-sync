from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TestPerson
from .serializers import TestPersonSerializer


class TestPersonView(APIView):
    def get(self, request):
        persons = TestPerson.objects.filter(is_deleted=False).order_by('-id')
        serializer = TestPersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = TestPersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            person = TestPerson.objects.get(pk=pk, is_deleted=False)
        except TestPerson.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = TestPersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

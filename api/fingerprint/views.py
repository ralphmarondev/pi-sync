from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FingerprintTemplate
from .serializers import FingerprintTemplateSerializer

# /fingerprint/  ➔ List all
class FingerprintListView(APIView):
    def get(self, request):
        templates = FingerprintTemplate.objects.filter(is_deleted=False, is_assigned=False)
        serializer = FingerprintTemplateSerializer(templates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# /fingerprint/enroll/  ➔ Enroll (register)
class FingerprintEnrollView(APIView):
    def post(self, request):
        serializer = FingerprintTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /fingerprint/details/<name>/  ➔ Get by name
class FingerprintDetailView(APIView):
    def get(self, request, name):
        try:
            template = FingerprintTemplate.objects.get(name=name, is_deleted=False)
            serializer = FingerprintTemplateSerializer(template)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FingerprintTemplate.DoesNotExist:
            return Response({'detail': 'Template not found.'}, status=status.HTTP_404_NOT_FOUND)

# /fingerprint/assign/  ➔ Update is_assigned to True when assigned
class FingerprintAssignView(APIView):
    def patch(self, request, name):
        try:
            # Get the fingerprint template by name
            template = FingerprintTemplate.objects.get(name=name, is_deleted=False)
            template.is_assigned = True
            template.save()

            # Return the updated template data
            serializer = FingerprintTemplateSerializer(template)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FingerprintTemplate.DoesNotExist:
            return Response({'detail': 'Template not found.'}, status=status.HTTP_404_NOT_FOUND)
    
# /fingerprint/unassign/<name>/  ➔ Set is_assigned = False
class FingerprintUnassignView(APIView):
    def patch(self, request, name):
        try:
            template = FingerprintTemplate.objects.get(name=name, is_deleted=False)
            template.is_assigned = False
            template.save()

            serializer = FingerprintTemplateSerializer(template)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FingerprintTemplate.DoesNotExist:
            return Response({'detail': 'Template not found.'}, status=status.HTTP_404_NOT_FOUND)

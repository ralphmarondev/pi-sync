from rest_framework import serializers

from .models import History

class HistorySerializer(serializers.ModelSerializer):
    room_name = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = History
        fields = '__all__'

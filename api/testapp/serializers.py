from rest_framework import serializers

from .models import TestPerson


class TestPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPerson
        fields = '__all__'

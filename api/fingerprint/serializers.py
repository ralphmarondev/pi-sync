from rest_framework import serializers
from .models import FingerprintTemplate

class FingerprintTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerprintTemplate
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', 'is_deleted']

    # def create(self, validated_data):
    #     return FingerprintTemplate.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.template = validated_data.get('template', instance.template)
    #     instance.save()
    #     return instance

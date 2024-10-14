from rest_framework import serializers

from .models import FamilyMember


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        family_member = FamilyMember(**validated_data)
        family_member.set_password(validated_data['password'])
        family_member.save()
        return family_member

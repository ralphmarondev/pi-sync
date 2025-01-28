from rest_framework import serializers

from rooms.models import Door
from .models import User

class UserSerializer(serializers.ModelSerializer):
	registered_doors = serializers.PrimaryKeyRelatedField(
		queryset=Door.objects.all(),
		many=True,
		required=False
	)

	class Meta:
		model = User
		fields = '__all__'

		extra_kwargs = {
			'password': {'write_only': True}
		}

	def create(self, validated_data):
		doors = validated_data.pop('registered_doors', [])
		user = super().create(validated_data)
		if doors:
			user.registered_doors.set(doors)
		return user

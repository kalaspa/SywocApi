from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from boats.models import Boat, Crewmate

class UserSerializer(serializers.ModelSerializer):
	boats = serializers.PrimaryKeyRelatedField(many=True, queryset=Boat.objects.all())
	crew = serializers.PrimaryKeyRelatedField(many=True, queryset=Crewmate.objects.all())

	class Meta:
		model = get_user_model()

from rest_framework import serializers
from django.contrib.auth import get_user_model

from boats.models import Boat , Crewmate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	boats = serializers.PrimaryKeyRelatedField(many=True, queryset=Boat.objects.all())
	crew = serializers.PrimaryKeyRelatedField(many=True, queryset=Crewmate.objects.all())

	class Meta:
		model = get_user_model()

class BoatSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Boat
		fields = ('id' , 'name' , 'university' , 'owner' )

class CrewmateSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Crewmate
		fields = ('firstname' , 'lastname' , 'boat' , 'owner')

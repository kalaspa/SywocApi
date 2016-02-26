from rest_framework import serializers
from boats.models import Boat , Crewmate

class BoatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Boat

class CrewmateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Crewmate

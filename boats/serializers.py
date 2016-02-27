from rest_framework import serializers
from boats.models import Boat , Crewmate

class BoatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Boat
		fields = ('id' , 'name' , 'university')

class CrewmateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Crewmate
		fields = ('firstname' , 'lastname' , 'boat')

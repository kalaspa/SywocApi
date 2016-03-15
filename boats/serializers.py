from rest_framework import serializers

from boats.models import Boat , Crewmate


class BoatSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Boat
		fields = ('id' , 'name' , 'university' , 'payment' , 'owner' )
		read_only_fields = ('payment',)

class CrewmateSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Crewmate
		fields = ('id' , 'firstname' , 'lastname' , 'boat' , 'owner')

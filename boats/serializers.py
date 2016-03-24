from rest_framework import serializers

from boats.models import Boat , Crewmate


class BoatSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Boat
		fields = ('id' , 'name' , 'university' , 'payment1' ,'payment2', 'owner', 'abandon' )
		read_only_fields = ('payment1', 'payment2', 'abandon',)

class CrewmateSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Crewmate
		fields = ('id' , 'firstname' , 'lastname' , 'boat' , 'owner')

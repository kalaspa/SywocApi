from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAdminUser
from rest_framework.decorators import detail_route, list_route

from boats.models import Boat , Crewmate
from boats.serializers import BoatSerializer , CrewmateSerializer
from users.permissions import IsOwnerOrReadOnly
# Create your views here.


class BoatViewSet (viewsets.ModelViewSet):
	queryset = Boat.objects.all()
	serializer_class = BoatSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	@list_route()
	def myboat(self, request):
		boat = Boat.objects.all().filter(owner=request.user)
		serialized = self.get_serializer(boat, many=True)
		return Response(serialized.data)

	@detail_route(methods=['POST'], permission_classes=[IsAdminUser,])
	def pay1(self, request, pk=None):
		boat = Boat.objects.all().filter(id=pk)[0]
		if boat.payment1 == None:
			boat.payment1 = True
		else:
			boat.payment1 ^= True
		boat.save()
		return Response('Payment changed')

	@detail_route(methods=['POST'], permission_classes=[IsAdminUser,])
	def pay2(self, request, pk=None):
		boat = Boat.objects.all().filter(id=pk)[0]
		if boat.payment2 == None:
			boat.payment2 = True
		else:
			boat.payment2 ^= True
		boat.save()
		return Response('Payment changed')

	@detail_route(methods=['POST'], permission_classes=[IsAdminUser,])
	def abandon(self, request, pk=None):
		boat = Boat.objects.all().filter(id=pk)[0]
		if boat.abandon == None:
			boat.abandon = True
		else:
			boat.abandon ^= True
		boat.save()
		return Response('Abandon changed')

class CrewmateViewSet (viewsets.ModelViewSet):
	queryset = Crewmate.objects.all()
	serializer_class = CrewmateSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	@list_route()
	def mycrew(self, request):
		crew = Crewmate.objects.all().filter(owner=request.user)
		serialized = self.get_serializer(crew, many=True)
		return Response(serialized.data)

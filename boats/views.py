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
	def pay(self, request, pk=None):
		boat = Boat.objects.all().filter(id=pk)[0]
		if boat.payment == None:
			boat.payment = True
		else:
			boat.payment ^= True
		boat.save()
		return Response('Payment changed')

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

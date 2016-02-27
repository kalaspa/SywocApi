from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from boats.models import Boat , Crewmate
from boats.serializers import BoatSerializer , CrewmateSerializer
from boats.permissions import IsOwnerOrReadOnly
# Create your views here.

class BoatViewSet (viewsets.ModelViewSet):
	queryset = Boat.objects.all()
	serializer_class = BoatSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	@detail_route(methods=['post'])
	def pay(self, request, pk=None):
		try:
			boat = Boat.objects.get(id=pk)
		except Boat.DoesNotExist:
			return HttpResponse(status=404)

		boat.payment = True
		boat.save()
		return Response({'status': 'payment set'})

	@list_route()
	def deleted(self, request):
		deleted = Boat.objects.all().filter(deleted=True)
		serializer = self.get_serializer(deleted, many=True)
		return Response(serializer.data)

	@list_route()
	def names(self, request):
		names = [ b.name for b in Boat.objects.all().filter(deleted=True)]
		return Response(names)

	@detail_route(methods=['post'])
	def add(self,request,pk=None):
		name, crew = request.data.get('name') , request.data.get('crew')
		boat = Boat.objects.get_or_create(name=name,category=category)
		return Response({'status': 'Boat created'})

class CrewmateViewSet (viewsets.ModelViewSet):
	queryset = Crewmate.objects.all()
	serializer_class = CrewmateSerializer

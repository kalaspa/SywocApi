from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAdminUser
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from boats.models import Boat , Crewmate
from boats.serializers import BoatSerializer , CrewmateSerializer , UserSerializer
from boats.permissions import IsOwnerOrReadOnly
# Create your views here.

class UserViewSet (viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAdminUser,)

class BoatViewSet (viewsets.ModelViewSet):
	queryset = Boat.objects.all()
	serializer_class = BoatSerializer
	#permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class CrewmateViewSet (viewsets.ModelViewSet):
	queryset = Crewmate.objects.all()
	serializer_class = CrewmateSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

@api_view(['POST'])
def create_auth(request):
	serialized = UserSerializer(data=request.data)
	if serialized.is_valid():
		User.objects.create_user(
			serialized.data['username'],
			serialized.data['email'],
			serialized.data['password']
		)
		return Response(serialized.data, status=status.HTTP_201_CREATED)
	else:
		return Response(serialized._errors , status=status.HTTP_400_BAD_REQUEST)

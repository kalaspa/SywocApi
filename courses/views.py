from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAdminUser

from courses.models import Course , Ranking
from courses.serializers import CourseSerializer , RankingSerializer
from users.permissions import IsAdminOrReadOnly
# Create your views here.


class CourseViewSet (viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	permission_classes = (IsAdminOrReadOnly,)


class RankingViewSet (viewsets.ModelViewSet):
	queryset = Ranking.objects.all()
	serializer_class = RankingSerializer
	permission_classes = (IsAdminOrReadOnly,)

"""sywocApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include , url
from django.contrib import admin
from rest_framework import routers
from boats.views import BoatViewSet , CrewmateViewSet
from users.views import  UserViewSet
from courses.views import CourseViewSet, RankingViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'boats', BoatViewSet)
router.register(r'crewmates', CrewmateViewSet)
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'rankings', RankingViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^register/', 'users.views.create_auth'),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

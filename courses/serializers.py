from rest_framework import serializers

from courses.models import Course, Ranking


class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Course
		fields = ('id' , 'name', 'date')

class RankingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Ranking
		fields = ('id' , 'course', 'boat', 'rank')

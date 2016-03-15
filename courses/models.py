from django.db import models
from boats.models import Boat

# Create your models here.
class Course (models.Model):

    name = models.CharField(max_length=50)
    date = models.DateField()


class Ranking (models.Model):

    boat = models.ForeignKey(Boat)
    course = models.ForeignKey(Course)

    rank = models.IntegerField()

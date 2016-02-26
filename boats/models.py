from django.db import models

# Create your models here.

class Crewmate (models.Model):

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    def __str__(self):
        return "{0} {1}".format(self.lastname , self.firstname)

class Boat (models.Model):

    name = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    email = models.EmailField()

    number = models.IntegerField()
    crew = models.ManyToManyField(Crewmate)

    payment = models.BooleanField(null=False)
    ranking = models.IntegerField(null=0)
    score = models.IntegerField(null=0)

    deleted = models.BooleanField(null=False)

    def __str__(self):
        return "{0} {1} {0}".format(self.name , self.university , self.email)

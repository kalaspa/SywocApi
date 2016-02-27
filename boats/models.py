from django.db import models

# Create your models here.
class Boat (models.Model):

    owner = models.ForeignKey('auth.User', related_name='boats')

    name = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    email = models.EmailField()

    payment = models.BooleanField(null=True)
    score = models.IntegerField(null=True)

    deleted = models.BooleanField(null=True)

    def __str__(self):
        return "{0} {1} {0}".format(self.name , self.university , self.email)

class Crewmate (models.Model):

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    boat = models.ForeignKey(Boat)

    def __str__(self):
        return "{0} {1}".format(self.lastname , self.firstname)

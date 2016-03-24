from django.db import models

# Create your models here.
class Boat (models.Model):

    owner = models.ForeignKey('auth.User', related_name='boats')

    name = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    email = models.EmailField()

    payment1 = models.NullBooleanField()
    payment2 = models.NullBooleanField()
    abandon = models.NullBooleanField()
    score = models.IntegerField(null=True)

    deleted = models.NullBooleanField()

    def __str__(self):
        return "{0} {1}".format(self.name , self.university)

class Crewmate (models.Model):

    owner = models.ForeignKey('auth.User', related_name='crew')

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    boat = models.ForeignKey(Boat)

    def __str__(self):
        return "{0} {1}".format(self.lastname , self.firstname)

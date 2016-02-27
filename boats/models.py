from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#Allow users to receive an authentication token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Boat (models.Model):

    owner = models.ForeignKey('auth.User', related_name='boats')

    name = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    email = models.EmailField()

    payment = models.NullBooleanField()
    score = models.IntegerField(null=True)

    deleted = models.NullBooleanField()

    def __str__(self):
        return "{0} {1} {0}".format(self.name , self.university , self.email)

class Crewmate (models.Model):

    owner = models.ForeignKey('auth.User', related_name='crew')

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    boat = models.ForeignKey(Boat)

    def __str__(self):
        return "{0} {1}".format(self.lastname , self.firstname)

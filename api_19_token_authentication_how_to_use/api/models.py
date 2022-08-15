from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings

from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

# for generate token
# token authentication using signals
# this signal creates auth token for user
# this will create token automatically when the user created


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **Kwargs):
    if created:
        Token.objects.create(user=instance)

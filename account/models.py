from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings

USER_STATUS_CHOICES = (
  ('O', 'Online'),
  ('A', 'Away'),
  ('B', 'Busy'),
  ('OF', 'Offline'),
  ('C', 'Custom'),
)

class UserInfo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='userprofile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, default=None)
    user_location = models.CharField(max_length=60, default=None)
    user_online_status = models.CharField(max_length=200, default="A", choices=USER_STATUS_CHOICES)
    user_post_status = models.CharField(max_length=300, default=None)


# Will run everytime a new user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
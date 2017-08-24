from django.db import models
from django.contrib.auth.models import User

class ConnectionInvite(models.Model):
    from_user = models.ForeignKey(User, related_name='connectioninvite_from_user')
    to_user = models.CharField(max_length=300, blank=True)
    message = models.CharField(max_length=300, blank=True)
    timestamp = models.DateTimeField(auto_now=True)


class ConnectionManager(models.Manager):
    def connections_for_user(self, user):
        return super(ConnectionManager, self).get_queryset().filter(
            Q(first_user=user.id) | Q(second_user=user.id))

    def new_connection(self, connection):
        new_connection = Connection(
            first_user = connection.to_user,
            second_user = connection.from_user,)

class Connection(models.Model):
    first_user = models.ForeignKey(User, related_name='connectusers_first_user')
    second_user = models.ForeignKey(User, related_name='connectusers_second_player')
    date_first_connected = models.DateTimeField(auto_now=True)
    objects = ConnectionManager()
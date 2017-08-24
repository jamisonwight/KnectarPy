from django.conf.urls import url

from .views import search_users, new_connection, accept_connection

urlpatterns = [
  url(r'^search/$', search_users, name="connections_user_search"),
  url(r'^invite/$', new_connection , name="connections_new_connection"),
  url(r'^accept/$', accept_connection, name="connections_accept_connection"),
]
from django.conf.urls import url
from account.views import home, UserProfile, UserUpdate, UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^home$', home, name='account_home'),
    url(r'^api/$', UserProfile.as_view(), name='account_user_profile'),
    url(r'^api/(?P<pk>[0-9]+)$', UserUpdate.as_view(), name='account_user_update'),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
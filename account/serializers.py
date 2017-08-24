from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo

class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserInfo
        fields = ('id', 'first_name', 'user_location', 'user_online_status','user_post_status','owner')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username')



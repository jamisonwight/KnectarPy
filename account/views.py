from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view
from account.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response


from tictactoe.models import Game
from .models import UserInfo

@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.filter(status="A")
    finished_games = my_games.exclude(status="A")
    waiting_games = active_games.filter(next_to_move=request.user)
    other_games = active_games.exclude(next_to_move=request.user)
    invitations = request.user.invitations_recieved.all()

    context = {
        'other_games': other_games,
        'waiting_games': waiting_games,
        'finished_games': finished_games,
        'invitations': invitations
    }

    return render(request, 'account/home.html', context)


# API Views
from .serializers import UserSerializer, UserProfileSerializer
 
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

     
class UserProfile(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                         IsOwnerOrReadOnly)


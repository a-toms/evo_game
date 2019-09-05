from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlayerSerializer
from .models import Player


class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

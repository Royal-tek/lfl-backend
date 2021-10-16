from django.shortcuts import render

from rest_framework import generics
from .serializers import PlayerSerializer, PlayerCreateSerializer, PointListSerializer, AwardPointSerializer
from .models import Player, Point

class PlayerListView(generics.ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerCreate(generics.ListCreateAPIView):
    serializer_class = PlayerCreateSerializer
    queryset = Player.objects.all()

class PointListView(generics.ListAPIView):
    serializer_class = PointListSerializer
    queryset = Point.objects.all()

class AwardPoint(generics.ListCreateAPIView):
    serializer_class = AwardPointSerializer
    queryset = Point.objects.all()
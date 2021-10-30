from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import generics
from .serializers import PlayerSerializer, UserSerializer, PlayerCreateSerializer,ListCoachSerializer, CoachUserSerializer, CreateTeamSerializer,NewsSerializer, PointListSerializer, AwardPointSerializer
from .models import Player, Point, UserTeam, News, Coach
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class PlayerListView(APIView):
    def get(self, request):
        authentication_classes = [TokenAuthentication, SessionAuthentication,]
        permission_classes = [IsAuthenticated]
        player = UserTeam.objects.all().filter(user=request.user)
        serializer = CreateTeamSerializer(player, many=True)
        return Response(serializer.data)


class ListAllPlayers(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        
        player = Player.objects.all().filter(approved=True)
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)


class LoggedUser(APIView):
    def get(self, request):
        user = User.objects.all().filter(username=request.user.username)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class CoachPlayers(APIView):
    def get(self, request):
        authentication_classes = [TokenAuthentication, SessionAuthentication,]
        permission_classes = [IsAdminUser]
        user = User.objects.all().filter(username=request.user.username)
        serializer = CoachUserSerializer(user, many=True)
        return Response(serializer.data)




class PlayerCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlayerCreateSerializer
    queryset = Player.objects.all()

class PointListView(generics.ListAPIView):
    serializer_class = PointListSerializer
    queryset = Point.objects.all()

class AwardPoint(generics.ListCreateAPIView):
    serializer_class = AwardPointSerializer
    queryset = Point.objects.all()



# class CreateTeam(APIView):
#     def get(self, request):
#         teams = UserTeam.objects.all()
#         serializer = CreateTeamSerializer(teams, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CreateTeamSerializer(data = request.data)
#         if serializer.is_Valid():
#             serializer.save()
#             return Response(serializer.data, status =status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateTeam(generics.ListCreateAPIView):
    queryset = UserTeam.objects.all()
    serializer_class = CreateTeamSerializer

class News(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

class ListAllCoaches(APIView):
    permission_classes = [AllowAny]
    def get(self, request):

        coach = Coach.objects.all()
        serializer = ListCoachSerializer(coach, many=True)
        return Response(serializer.data)

from rest_framework import serializers
from .models import *


class coachSerializer(serializers.ModelSerializer):
    class Meta:
        model= Coach
        fields ='__all__'


#This is the serializer for listing all the available and approved players in the model.
#NOTE --------- THE SERIALIZER SHOULD ONLY LIST APPROVED PLAYERS, REMEMBER TO PUT THAT FUNCTIONALITY
class PlayerSerializer(serializers.ModelSerializer):
    coach = coachSerializer(read_only=True)
    class Meta:
        model = Player
        fields = ['id','coach','firstname','lastname', 'username', 'position', 'team', 'status', 'date_created']


#This is the serializer for creating and registration of a player...
class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','coach','firstname','lastname', 'username', 'position', 'team', 'status', 'date_created']
        read_only_fields = ['date_created', 'status']

#This is the serializer for listing all the points of a player
class PointListSerializer(serializers.ModelSerializer):
    player = PlayerCreateSerializer(read_only=True)
    class Meta:
        model = Point
        fields = ['id','player', 'goals', 'assists', 'minutes_played', 'yellowcard', 'redcard', 'weekday', 'captain']
        
#This is the serializer for enabling accreditation of points
class AwardPointSerializer(serializers.ModelSerializer):
    # player = PlayerCreateSerializer(read_only=True)
    class Meta:
        model = Point
        fields = ['id','player', 'goals', 'assists', 'minutes_played', 'yellowcard', 'redcard', 'weekday', 'captain']
        
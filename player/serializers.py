from rest_framework import serializers
from .models import *



#This is the serializer for enabling accreditation of points
class AwardPointSerializer(serializers.ModelSerializer):
    # player = PlayerCreateSerializer(read_only=True)
    class Meta:
        model = Point
        fields = ['id','player', 'goals', 'assists', 'minutes_played', 'yellowcard', 'redcard', 'week', 'captain']
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerImage
        fields = ['image']
    def validate(self, attrs):
        return attrs
    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

#This is the serializer for listing all the available and approved players in the model.
#NOTE --------- THE SERIALIZER SHOULD ONLY LIST APPROVED PLAYERS, REMEMBER TO PUT THAT FUNCTIONALITY

class player(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
class coachSerializer(serializers.ModelSerializer):
    coach = player(read_only=True, many=True)
    class Meta:
        model= Coach
        fields ='__all__'

class PlayerSerializer(serializers.ModelSerializer):
    coach = coachSerializer(read_only=True)
    playerpoint = AwardPointSerializer(read_only=True, many=True)
    playerimage = ImageSerializer(read_only=True, many=True)
    class Meta:
        model = Player
        fields = ['id','coach','firstname','playerimage','lastname', 'username','playerpoint', 'position', 'team', 'approved', 'date_created']

class PlayerDisplaySerializer(serializers.ModelSerializer):
    # coach = coachSerializer(read_only=True)
    playerpoint = AwardPointSerializer(read_only=True, many=True)
    playerimage = ImageSerializer(read_only=True, many=True)
    class Meta:
        model = Player
        fields = ['id','firstname','playerimage','lastname', 'username','playerpoint', 'position', 'team', 'approved', 'date_created']



#This is the serializer for creating and registration of a player...
class PlayerCreateSerializer(serializers.ModelSerializer):
    playerimage = ImageSerializer(write_only=True)
    class Meta:
        model = Player
        fields = ['id','coach','firstname','lastname','playerimage', 'username', 'position', 'number', 'team', 'college', 'approved', 'date_created']
        read_only_fields = ['date_created', 'approved']
    def validate(self, attrs):
        return attrs
    def create(self, validated_data):
        queryset =None
        if validated_data["playerimage"]:
            seriali_image = ImageSerializer
            s_image = seriali_image(data=validated_data["playerimage"])
            del validated_data["playerimage"]
        queryset = self.Meta.model.objects.create(**validated_data)
        s_image.is_valid(raise_exception = True)
        s_image.save(player=queryset)
        return queryset

#This is the serializer for listing all the points of a player
class PointListSerializer(serializers.ModelSerializer):
    player = PlayerCreateSerializer(read_only=True)
    class Meta:
        model = Point
        fields = ['id','player', 'goals', 'assists', 'minutes_played', 'yellowcard', 'redcard', 'week', 'captain']

class CoachUserSerializer(serializers.ModelSerializer):
    coachuser = coachSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['id', 'username','coachuser', 'first_name', 'last_name', 'email', 'is_staff']   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff']

class UserTeamSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    attackers = PlayerDisplaySerializer(read_only = True, many=True)
    midfielders = PlayerDisplaySerializer(read_only = True, many=True)
    defenders = PlayerDisplaySerializer(read_only = True, many=True)
    goalkeeper  = PlayerDisplaySerializer(read_only = True, many=True)
    class Meta:
        model = UserTeam
        fields = ['id','user','attackers', 'midfielders', 'defenders', 'goalkeeper']
        read_only_field = 'user'

class CreateUserTeam(serializers.ModelSerializer):
    # user = UserSerializer(read_only= True)
    class Meta:
        model = UserTeam
        fields = ['id', 'user', 'attackers', 'midfielders', 'defenders', 'goalkeeper'] 

class approvePlayer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'approved']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image','title', 'poster', 'content','date','approved']
        # read_only_field =  ['approved',]


class ListCoachSerializer(serializers.ModelSerializer):
    code_team_user = UserSerializer(read_only=True)
    class Meta:
        model = Coach
        fields = ['code_team_user', 'team']
from django.urls import path
from .views import PlayerListView, approvePlayer,  PlayerCreate,ListAllCoaches, UserCreateTeam, PointListView, AwardPoint, ViewUserTeams, News, LoggedUser, ListAllPlayers, CoachPlayers, DisplayAllPlayers

urlpatterns = [
    path('listplayers/', PlayerListView.as_view()),
    path('createplayers/', PlayerCreate.as_view()),
    path('listpoints/', PointListView.as_view()),
    path('awardpoints/', AwardPoint.as_view()),
    path('userteams/', ViewUserTeams.as_view()),
    path('news/', News.as_view()),
    path('listallplayers/', ListAllPlayers.as_view()),
    path('viewuser/', LoggedUser.as_view()),
    path('coachplayers/', CoachPlayers.as_view()),
    path('listallcoaches/', ListAllCoaches.as_view()),
    path('displayplayers/', DisplayAllPlayers.as_view()),
    path('createteam/', UserCreateTeam.as_view()),
    path('approveplayer/<int:id>', approvePlayer.as_view()),


]

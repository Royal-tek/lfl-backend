from django.urls import path
from .views import PlayerListView, PlayerCreate,ListAllCoaches, PointListView, AwardPoint, CreateTeam, News, LoggedUser, ListAllPlayers, CoachPlayers

urlpatterns = [
    path('listplayers/', PlayerListView.as_view()),
    path('createplayers/', PlayerCreate.as_view()),
    path('listpoints/', PointListView.as_view()),
    path('awardpoints/', AwardPoint.as_view()),
    path('createteam/', CreateTeam.as_view()),
    path('news/', News.as_view()),
    path('listallplayers/', ListAllPlayers.as_view()),
    path('viewuser/', LoggedUser.as_view()),
    path('coachplayers/', CoachPlayers.as_view()),
    path('listallcoaches/', ListAllCoaches.as_view()),
]

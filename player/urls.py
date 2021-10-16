from django.urls import path
from .views import PlayerListView, PlayerCreate, PointListView, AwardPoint

urlpatterns = [
    path('listplayers/', PlayerListView.as_view()),
    path('createplayers/', PlayerCreate.as_view()),
    path('listpoints/', PointListView.as_view()),
    path('awardpoints/', AwardPoint.as_view()),
]
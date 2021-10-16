from django.contrib import admin



from .models import Player, PlayerImage, Coach, Point, UserTeam, Weeks


#This is for the arrangement and view of the database in a particular format.
class PointList(admin.ModelAdmin):
    model = Point
    list_display = ['player', 'goals', 'assists', 'minutes_played', 'yellowcard', 'redcard', 'week', 'weekly_points','total_points', 'captain']



admin.site.register(Player)
admin.site.register(PlayerImage)
admin.site.register(Coach)
admin.site.register(Point, PointList)
admin.site.register(UserTeam)
admin.site.register(Weeks)
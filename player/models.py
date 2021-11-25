from django.db import models
from django.contrib.auth.models import User

# This is for the different positions a player can pick 
positions = (
    ("fwd", "Foward"),
    ("mid", "Midfield"),
    ("def", "Defence"),
    ("gk", "Goal keeper"),
)

#This is for the different teams available on the app
teams = (
    ("cve","Civil Engineering"),
    ("mch","Mechanical Engineering"),
    ("csc","Computer Science"),
    ("abe","Agric and Biosystems Engineering"),
    ("sip","Sociology, International reltions and political science"),
    ("sos","School of Science"),
    ("phy","Physical Sience"),
    ("eie","Electrical Information Engineering"),
    ("acc","Accounting"),
    ("eco","Economics"),
    ("mcom","Mass Communication"),
    ("aqua","Agric Extention"),
    ("cas","Animal Science"),
    ("chem","Chemical Engineering"),
    ("bus","Business Admin"),
)

#This is for the different weeks available on the app
weekday = (
    ("wk1", "week1"),
    ("wk2", "week2"),
    ("wk3", "week3"),
    ("wk4", "week4"),
    ("wk5", "week5"),
    ("wk6", "week6"),
    ("wk7", "week7"),
    ("wk8", "week8"),
    ("wk9", "week9"),
    ("wk10", "week10")
)

# This is for the colleges selection and option
college = (
    ("cpas", "College of pure and applied science"),
    ("coe", "College of Engineering"),
    ("cas", "College of Agricultural Science"),
    ("cbs", "College of Business and Social Science")
)

#This is the selection for the number of cards a player recieved
card = (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3")
)


#This is the coach model, every player must be validated and approved by his coach. So when a player is registering , he would have to also specify who his coach is and if his coach approves that he is ne of his player then the player status will change to true enabling him to be displayed in the app.
class Coach(models.Model):
    code_team_user = models.ForeignKey(User, related_name="coachuser", on_delete=models.CASCADE)
    team = models.CharField(max_length=5, choices=teams)

    def __str__(self):
        return self.code_team_user.username
    
    class Meta:
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'
    
#This is the player model, where the players would be registered to and specify who their coach is so they can wait for approval.
class Player(models.Model):
    coach = models.ForeignKey(Coach, related_name='coach', on_delete= models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    position = models.CharField(max_length=3, choices=positions, default=2)
    number = models.IntegerField(null=True)
    college = models.CharField(max_length=200, null=True, choices=college)
    team = models.CharField(max_length=5, choices=teams, blank=True)
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True, auto_created=False)

    def __str__(self):
        return  "{0}".format(self.firstname)

    class Meta:
        ordering = ['date_created']

#This is the model for the a particular users team. A user a foreign key to this particular model, It has a many to many field that contains all the players in the player model and allows you to pick 23 players.
class UserTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attackers = models.ManyToManyField(Player, related_name='attackers')
    midfielders = models.ManyToManyField(Player,  related_name='midfielders')
    defenders = models.ManyToManyField(Player,  related_name='defenders')
    goalkeeper = models.ManyToManyField(Player,  related_name='goalkeeper')

    def __str__(self):
        return self.user.username

#This is the player image model which has a foreign key to the player model , it is for a particular players image
class PlayerImage(models.Model):
    player = models.ForeignKey(Player, related_name="playerimage", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return "{} ".format(self.player.username)

#This is the model for the weeks in the session
class Weeks(models.Model):
    weekday = models.CharField(max_length=10, default=1, choices=weekday)

    def __str__(self):
        return self.weekday
    
    class Meta:
        verbose_name_plural = 'Weeks'


#This is for the points awardal. It contains the weekly points and the total points of a particular player . The player is referenced as a foreign key to the point model.
class Point(models.Model):
    player = models.ForeignKey(Player, related_name="playerpoint", on_delete = models.CASCADE)
    goals = models.IntegerField(blank=True, null=True)
    week = models.ForeignKey(Weeks, on_delete = models.CASCADE)
    assists = models.IntegerField(blank=True, null=True, default=0)
    minutes_played = models.IntegerField(blank=True)
    yellowcard = models.CharField(max_length=10, default=0, choices = card)
    redcard = models.CharField(max_length=10, default=0, choices = card)
    captain = models.BooleanField()
    weekly_points = models.IntegerField(default=1)
    total_points = models.IntegerField(default=1)


    class Meta:
        verbose_name_plural = 'Points'
        ordering = ['total_points']

    def __str__(self):
        return self.player.username

    def save(self, *args, **kwargs):

        if self.player.position == 'mid' and self.goals > 2:
            self.total_points = 200
            

        # if self.goals> 2:
        #     self.weekly_points = 10
        # self.total_points = self.weekly_points*2
        super(Point, self).save(*args, **kwargs)

class News(models.Model):
    image = models.FileField(upload_to='media')
    title = models.CharField(max_length=200)
    poster = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-date']
        verbose_name = 'News'
    
    def __str__(self):
        return self.title
    
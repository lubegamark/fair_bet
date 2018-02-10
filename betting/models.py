from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GameWeek(models.Model):
    start_time = models.DateTimeField()
    name = models.IntegerField()

    def __str__(self):
        return "Gameweek {}".format(self.name)


class Game(models.Model):
    game_week = models.ForeignKey(GameWeek, related_name='games')
    time = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name='home_team')
    away_team = models.ForeignKey(Team, related_name='away_team')
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)

    def final_scores(self):
        if self.home_score is not None and self.away_score is not None:
            return "{} {} - {} {}".format(self.home_team,
                                          self.home_score,
                                          self.away_score,
                                          self.away_team)
        else:
            return "-"

    def __str__(self):
        return "{} vs {}".format(self.home_team, self.away_team)


class Prediction(models.Model):
    user = models.ForeignKey(User, related_name='predictions')
    game = models.ForeignKey(Game, related_name='predictions')
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def __str__(self):
        return "{} : {} {} vs {} {}".format(self.user,
                                            self.game.home_team,
                                            self.home_score,
                                            self.away_score,
                                            self.game.away_team)

    def point(self):
        if (self.home_score == self.game.home_score and
                    self.away_score == self.game.away_score):
            return 1
        return 0

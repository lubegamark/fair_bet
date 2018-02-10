from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import betting


class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments')
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {} ".format(self.user, self.amount)


class GameWeekBet(models.Model):
    game_week = models.ForeignKey(betting.models.GameWeek, related_name='bets')
    user = models.ForeignKey(User, related_name='bets')
    amount = models.IntegerField()

    def __str__(self):
        return "{} : {} ".format(self.user, self.game_week)


class Winning(models.Model):
    game_week = models.ForeignKey(betting.models.GameWeek,
                                  related_name='winnings')
    user = models.ForeignKey(User, related_name='winnings')
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {} - {}".format(self.user, self.game_week, self.amount)

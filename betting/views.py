from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now

from betting.models import Game, Prediction, GameWeek



def home(request):
    if request.method == 'GET':
        if request.user:
            return render(request, 'home.html', {"games": games,
                                                 "game_week": game_week,
                                                 "game_week_done": done})


def game_week(request, game_week):
    if request.method == 'GET':
        if request.user:
            g_w = GameWeek.objects.filter(name=game_week).first()
            done = True
            if g_w.start_time > now():
                done = False
            games = Game.objects.filter(game_week__name=game_week).all()
            predictions = Prediction.objects.filter(game__game_week__name=game_week,
                                                    user=request.user).all()
            return render(request, 'gameweek.html', {"games": games,
                                                     "predictions": predictions,
                                                     "game_week": game_week,
                                                     "game_week_done": done})
        else:
            return render(request, 'gameweek.html', {})
    elif request.method == 'POST':
        pass



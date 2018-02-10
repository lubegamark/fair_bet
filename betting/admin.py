from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.db.models import Sum, F, Case, When, Q

from betting.models import GameWeek, Game, Prediction, Team


class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'point',
    )
    list_filter = (
        'user',
        'game__game_week',
    )
    search_fields = ('__str__',)


class GameAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'game_week',
        'final_scores',
    )
    list_filter = (
        'game_week',
    )
    search_fields = ('__str__',)


class UserPoints(User):
    class Meta:
        proxy = True
        verbose_name = 'Points'
        verbose_name_plural = 'Points'


class UserPointsAdmin(ModelAdmin):
    list_display = ('__str__', 'balance',)

    def get_queryset(self, request):
        qs = super(UserPointsAdmin, self).get_queryset(request)
        return qs.annotate(balance=Sum('predictions__amount')-Sum(
            'bets__amount'))

    def balance(self, obj):
        return obj.points
    balance.short_description = 'Account Balance'


admin.site.register(GameWeek)
admin.site.register(Game, GameAdmin)
admin.site.register(Prediction, PredictionAdmin)
admin.site.register(Team)

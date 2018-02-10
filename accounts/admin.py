from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.db.models import Sum

from accounts.models import Payment, GameWeekBet, Winning


class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'user',
        'date'
    )
    list_filter = (
        'user',
    )
    search_fields = ('__str__',)


class AccountSummary(User):
    class Meta:
        proxy = True
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


class AccountAdmin(ModelAdmin):
    list_display = ('__str__', 'balance',)

    def get_queryset(self, request):
        qs = super(AccountAdmin, self).get_queryset(request)
        return qs.annotate(balance=(Sum('payments__amount')-Sum(
            'bets__amount')))

    def balance(self, obj):
        return obj.balance
    balance.short_description = 'Account Balance'


admin.site.register(Payment, PaymentsAdmin)
admin.site.register(Winning, PaymentsAdmin)
admin.site.register(AccountSummary, AccountAdmin)
admin.site.register(GameWeekBet)

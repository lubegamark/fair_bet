from django.conf.urls import url

from betting import views

urlpatterns = (
    url(r'(?P<game_week>[0-9]+)/$', views.game_week),
)

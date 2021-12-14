from django.db import models
from levelupapi.models.event import Event
from levelupapi.models.game_type import GameType


class Game(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(
        Event, verbose_name="event", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(GameType, verbose_name="game_type", on_delete=models.SET_NULL, null=True)
                               

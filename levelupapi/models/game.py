from django.db import models
from levelupapi.models.event import Event
from levelupapi.models.game_type import Game_Type


class Game(models.Model):
    name = models.CharField(max_length=50)
    event_id = models.ForeignKey(
        Event, verbose_name="event", on_delete=models.SET_NULL, null=True)
    type_id = models.ForeignKey(Game_Type, verbose_name="game_type", on_delete=models.SET_NULL, null=True)
                               

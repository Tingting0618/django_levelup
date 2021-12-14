from django.db import models
from levelupapi.models.event import Event
from levelupapi.models.gamer import Gamer

class Player(models.Model):
    event = models.ForeignKey(
        Event, verbose_name="event", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        Gamer, verbose_name="gamer", on_delete=models.SET_NULL, null=True)
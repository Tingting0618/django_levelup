from django.db import models
from levelupapi.models.event import Event
from levelupapi.models.gamer import Gamer

class Player(models.Model):
    event_id = models.ForeignKey(
        Event, verbose_name="event", on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(
        Gamer, verbose_name="gamer", on_delete=models.SET_NULL, null=True)
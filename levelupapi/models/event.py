from django.db import models
from levelupapi.models.gamer import Gamer


class Event(models.Model):
    creator_id = models.ForeignKey(
        Gamer, verbose_name="creator", on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=50)
    time = models.DateTimeField(("%Y-%m-%d %H:%M:%S"), auto_now=False, auto_now_add=True)
                               

from django.db import models


class Game_Type(models.Model):
    type_name = models.CharField(max_length=50)

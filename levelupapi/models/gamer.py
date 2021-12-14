from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    #models.set_default, default = 1  --- give the value of the foreign key id to 1
    #models.SET_NULL --- give null values to nothing
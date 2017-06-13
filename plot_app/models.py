from django.db import models
from django.contrib.auth.models import User

# TODO: If any custom user information - make a custom user model

# Users can create teams
class Team(models.Model):
    name = models.CharField(max_length=64)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


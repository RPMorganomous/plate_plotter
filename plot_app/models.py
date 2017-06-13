from django.db import models
from django.contrib.auth.models import User

DEFAULT_LENGTH = 64

# TODO: If any custom user information - make a custom user model

MEAL_TAGS_CHOICES = (
    ('DEF', 'No Tag'),
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('Sn', 'Snack'),
    ('Sup', 'Supplement'),
    ('C', 'Cheat'),
    ('T', 'Tasty'),
    ('Y', 'Yuck!'),
    ('HC', 'High Calorie'),
    ('LC', 'Low Calorie')
)


# Users can create teams
class Team(models.Model):
    name = models.CharField(max_length=DEFAULT_LENGTH)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

# Upon making photo create the Meal Entry
class Meal(models.Model):
    name = models.CharField(max_length=DEFAULT_LENGTH)
    calories = models.PositiveSmallIntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(null=True)  # For now can be empty
    tags = models.CharField(choices=MEAL_TAGS_CHOICES, default="DEF")

    def __str__(self):
        return self.name

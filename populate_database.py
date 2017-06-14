import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'plate_plotter.settings')

import django

django.setup()

import random
from django.contrib.auth.models import User
from plot_app.models import Team, Meal, MEAL_TAGS_CHOICES
from faker import Faker

fakegen = Faker()
TEAMS_NAMES = ['A-Team', 'Super Team', 'The Losers', 'Starve Or Die', 'Suck-It-Up']


def add_team(name):
    """Right now the function doesn't assign any ManyToMany relationships"""
    # TODO Fix ManyToMany assignment
    t = Team.objects.get_or_create(name=name)[0]
    t.save()
    return t


def add_user(username, first_name, last_name, email):
    u = User.objects.get_or_create(username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email)[0]
    u.save()
    return u


def add_meal(user, calories, date, tag, photo=None):
    m = Meal.objects.get_or_create(user=user,
                                   calories=calories,
                                   date=date,
                                   tag=tag,
                                   photo=photo)[0]
    m.save()
    return m


def populate(users_count=1, teams_count=1, meals_count=1):
    for users in range(users_count):
        username = fakegen.user_name()
        name = fakegen.name().split()
        first_name, last_name = name[0], name[1]
        email = fakegen.email()

        # new user entry
        user = add_user(username, first_name, last_name, email)
        print('{}: User is added'.format(user.username))

    for teams in range(teams_count):
        team = add_team(random.choice(TEAMS_NAMES))
        print('{}: Team is added'.format(team.name))

    for meals in range(meals_count):
        user = User.objects.order_by('?').first()
        meal = add_meal(user, random.randint(10, 4000), fakegen.date(), random.choice(MEAL_TAGS_CHOICES))
        print('{}: Meal is added'.format(meal))


if __name__ == '__main__':
    print("POPULATING ZE DATABASE")
    populate(1, 1, 5)
    print("COMPLETE!")

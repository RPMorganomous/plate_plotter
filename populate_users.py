import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'plate_plotter.settings')

import django
django.setup()

import random
from django.contrib.auth.models import User
from plot_app.models import Team
from faker import Faker

fakegen = Faker()
teams = ['A-Team','Super Team','The Losers','Starve Or Die','Suck-It-Up']

def add_team():
    t = Team.objects.get_or_create(name=random.choice(teams))[0]
    t.save()
    return t

def populate(N=5):

    team = add_team()

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        fake_user = fakegen.user_name(*args, **kwargs)

        #new user entry
        user = User.objects.get_or_create(first_name = fake_first_name,
                                          last_name = fake_last_name,
                                          email = fake_email,
                                          username = fake_user)[0],

        team_rec = Team.objects.get_or_create(name=team,user=fake_user)

        i = 0
        while (i < 20):
            fake_cal = randint(10, 4000)
            fake_date = fakegen.date()
            fake_photo = "/images/plate-1.jpg"
            tag = random.choice(models.MEAL_TAGS_CHOICES)

            meal_rec = Meal.objects.get_orCreate(name=fake_name,
                                                 calories=fake_cal,
                                                 date=fake_date,
                                                 photo=fake_photo,
                                                 tags=tag)[0],

            i = i+1

if __name__ == '__main__':
    print("POPULATING ZE DATABASE")
    populate(20)
    print("COMPLETE!")


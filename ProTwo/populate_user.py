import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()
users = ['First Name', 'Last Name', 'Email']

# def add_name():
#     n = User.objects.get_or_create(first_name=random.choice(users))[0]
#     n.save()
#     return n


def populate(N=5):
    for entry in range(N):

        #Create the data for that entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # New entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('populating databases!')
    populate(20)
    print('populating complete!')


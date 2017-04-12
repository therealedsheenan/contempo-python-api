import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'contempo_python_api.settings')

import django
django.setup()

## FAKE SCRIPT
import random
from first_app.models import AccessRecord,WebPage,Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News' , 'Games']

def add_topic():
  t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
  t.save()
  return t

def populate(N=5):
  for entry in range(N):
    # get topic for the entry
    top = add_topic()

    # create fake data
    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()

    # create new webpage entry
    webpage = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


    # create access record
    acc_rec = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

def fake_users(N=5):
  for entry in range(N):
    fake_first_name = fakegen.name()
    fake_last_name = fakegen.name()
    fake_email = fakegen.email()

    # create fake user
    users = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
  print('populating script!')
  populate(0)
  fake_users(0)
  print('population complete')

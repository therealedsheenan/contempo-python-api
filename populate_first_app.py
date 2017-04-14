import os
import django
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'contempo_python_api.settings')
django.setup()

from first_app.models import AccessRecord, WebPage, Topic

# FAKE SCRIPT

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get topic for the entry
        top = add_topic()

        # create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new web_page entry
        web_page = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create access record
        acc_rec = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(0)
    print('population complete')

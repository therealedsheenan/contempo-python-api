from django.shortcuts import render
from first_app.models import AccessRecord


def index(request):
    web_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': web_list, 'site_name': 'Site Name'}
    return render(request, 'first_app/index.html', date_dict)


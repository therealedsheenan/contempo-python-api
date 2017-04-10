from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  my_dictionary = { "insert_me": "Hello I am python" }
  return render(request, 'first_app/index.html', context=my_dictionary)

def help(request):
  my_dictionary = { "help": "Help page" }
  return render(request, 'first_app/help.html', context=my_dictionary)
from django.shortcuts import render
from first_app.models import AccessRecord,User
from first_app.forms import NewUserForm

def index(request):
  webpages_list = AccessRecord.objects.order_by('date')
  date_dict = {'access_records': webpages_list}
  return render(request, 'first_app/index.html', context=date_dict)

def help(request):
  my_dictionary = { "help": "Help page" }
  return render(request, 'first_app/help.html', context=my_dictionary)

def users(request):
  users = User.objects.all
  my_dictionary = {'users': users }
  return render(request, 'first_app/users.html', context=my_dictionary)

def new_user(request):
  form = NewUserForm()

  if request.method == 'POST':
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print('Error Form invalid')

  return render(request, 'first_app/new_user.html', {'form': form})

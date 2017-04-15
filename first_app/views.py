from django.shortcuts import render
from django.contrib.auth.models import User
from first_app.models import AccessRecord, UserProfileInfo
from first_app.forms import NewUserForm, NewUserProfileForm

# authentication
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    web_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': web_list, 'site_name': 'Site Name'}
    return render(request, 'first_app/index.html', date_dict)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('index')


@login_required
def users(request):
    user_list = User.objects.all
    my_dictionary = {'users': user_list}
    return render(request, 'first_app/users.html', context=my_dictionary)


def registration(request):
    registered = False

    user_form = NewUserForm()
    user_profile_form = NewUserProfileForm()

    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        user_profile_form = NewUserProfileForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            return index(request)
        else:
            print(user_form.errors, user_profile_form.errors)
    else:
        user_form = NewUserForm()
        user_profile_form = NewUserProfileForm()

    return render(request, 'first_app/registration.html',
                  {'user_form': user_form,
                   'user_profile_form': user_profile_form,
                   'registered': registered})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/first_app/users')
            else:
                return HttpResponse("Account not active.")
        else:
            print("Invalid Credentials.")
            return HttpResponse("Invalid Credentials.")
    else:
        return render(request, 'first_app/login.html', {})

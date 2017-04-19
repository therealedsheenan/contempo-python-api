from django.shortcuts import render
from django.contrib.auth.models import User

from users.forms import NewUserForm, NewUserProfileForm

# authentication
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user_list = User.objects.all
    my_dictionary = {'users': user_list}
    return render(request, 'users/index.html', context=my_dictionary)


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/users/sign_in')


def sign_up(request):
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

    return render(request, 'users/sign_up.html',
                  {'user_form': user_form,
                   'user_profile_form': user_profile_form,
                   'registered': registered})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/users/')
            else:
                return HttpResponse("Account not active.")
        else:
            print("Invalid Credentials.")
            return HttpResponse("Invalid Credentials.")
    else:
        return render(request, 'users/sign_in.html', {})

from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.views import View

from users.forms import NewUserForm, NewUserProfileForm, SignInForm

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


class SignIn(View):

    @staticmethod
    def get(request):
        sign_in_form = SignInForm()
        context = {'sign_in_form': sign_in_form}
        return render(request, 'users/sign_in.html', context)

    @staticmethod
    def post(request):
        sign_in_form = SignInForm()
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/users/')
            else:
                print('Invalid Credentials.')
                return HttpResponse('Invalid Credentials')
        else:
            context = {'sign_in_form': sign_in_form}
            return render(request, 'users/sign_in.html', context)


class SignUp(View):

    @staticmethod
    def get(request):
        registered = False

        user_form = NewUserForm()
        user_profile_form = NewUserProfileForm()

        return render(request, 'users/sign_up.html',
                      {'user_form': user_form,
                       'user_profile_form': user_profile_form,
                       'registered': registered})

    @staticmethod
    def post(request):
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


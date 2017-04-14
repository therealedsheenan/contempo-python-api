from django.shortcuts import render
from django.contrib.auth.models import User
from first_app.models import AccessRecord, UserProfileInfo
from first_app.forms import NewUserForm, NewUserProfileForm


def index(request):
    web_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': web_list, 'site_name': 'Site Name'}
    return render(request, 'first_app/index.html', date_dict)


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
            user.save

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

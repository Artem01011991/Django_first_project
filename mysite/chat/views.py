from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserPageForm
from django.contrib.auth import authenticate, login, logout
from . import models


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            # Username and password should be received at raw form
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Logs in the user for current session
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            # First_name by default
            def_fname = request.user
            def_fname.first_name = 'unknown'
            def_fname.save()

            return redirect('/userpage/' + str(request.user.id))
    # Whether user have authenticated already
    elif request.user.is_authenticated:

        return redirect('/userpage/' + str(request.user.id))
    # Blank form have been passed
    else:
        form = RegistrationForm()

    users_names = models.UserAccount.objects.all()

    return render(request, 'chat/register_page.html', {'form': form, 'users_names': users_names})


def user_page(request, user_id):
    #  change photo
    if request.method == 'POST' and request.FILES['user_photo']:
        form = UserPageForm(request.POST, request.FILES, instance=request.user.useraccount)

        if form.is_valid():
            form.save()

            return redirect('/userpage/' + str(request.user.id))
        else:

            return render(request, 'chat/userpage.html', {'form': form, 'user_id': user_id})
    #  logout user condition
    if 'logout' in request.GET:
        logout(request)

        return redirect('/login/')
    # Check for whether existing user page.
    if models.UserAccount.objects.get(user=user_id):
        url_photo = models.UserAccount.objects.get(user=user_id)

        return render(request, 'chat/userpage.html', {'user_id': user_id, 'url_photo': url_photo})

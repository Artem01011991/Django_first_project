from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserPageForm
from django.contrib.auth import authenticate, login, logout


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

            return redirect('/userpage/')
    # Whether user have authenticated already
    elif request.user.is_authenticated():

        return redirect('/userpage/')
    # Blank form have been passed
    else:
        form = RegistrationForm()

    return render(request, 'chat/register_page.html', {'form': form})


def user_page(request):
    if request.method == 'POST' and request.FILES['user_photo']:
        form = UserPageForm(request.POST, request.FILES, instance=request.user.useraccount)

        if form.is_valid():
            form.save()

            return redirect('/userpage/')

    if 'logout' in request.GET:
        logout(request)

        return redirect(r'login/')

    if not request.user.is_authenticated():

        return redirect(r'login/')

    form = UserPageForm(instance=request.user)

    return render(request, 'chat/userpage.html', {'form': form})

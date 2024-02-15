from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def main(request):
    return render(request, 'app1/main.html')
def HomePage(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'app1/main.html', context)

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            User.objects.get(username=uname)
            messages.error(request, 'The username is already taken.')
            return HttpResponse("The username is already taken.")
        except User.DoesNotExist:
            my_user = User.objects.create_user(uname, email, pass1)
            print(my_user)
            my_user.save()
            login(request, my_user)
            return redirect('login_url')
    return render(request, 'registration.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username1')
        pass3 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass3)

        if user is not None:
            login(request, user)
            return redirect('home_url')
        else:
            return HttpResponse("Username or Password is wrong!!!")

    return render(request, 'signin.html')


def LogoutPage(request):
    logout(request)
    return redirect('login_url')

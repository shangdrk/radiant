from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'login/index.html', {})


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'login/index.html', {})
    else:
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']

        if username and password and first_name and last_name and email:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return HttpResponseRedirect("user/%s/" % username)
        else:
            return render(request, 'login/index.html', {
                'error_message': "Please fill out all blanks",
            })


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'login/signin.html', {})
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return render(request, 'login/signin.html', {
                'error_message': "Signin information is incorrect",
            })
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                return HttpResponseRedirect("../user/%s/" % username)
            else:
                return render(request, 'login/signin.html', {
                    'error_message': "Signin information is incorrect",
            })


def temp(reqeust, username):
    return HttpResponse("good!")

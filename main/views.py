from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from main.models import Personal
from .populate import feed


def profile(request, username):
    user = User.objects.get(username=username)
    if not hasattr(user, 'personal'):
        user.personal = Personal()

    if user.is_authenticated():
        json_data = feed()
        return render(request, 'main/profile.html', {
            'first_name': user.first_name,
            'json_data': json_data,
        })
    else:
        raise Http404("This page does not exist")

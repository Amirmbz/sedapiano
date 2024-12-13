from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from secrets import token_hex


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def profile(request):
    return render(request, 'home/profile.html')


def tprofile(request):
    return render(request, 'home/tprofile.html')


def person(request):
    return render(request, 'home/person.html')


def studyplan(request):
    return render(request, 'home/studyplan.html')


def indext(request):
    return render(request, 'home/indext.html')


def test(request):
    return render(request, 'home/test.html')

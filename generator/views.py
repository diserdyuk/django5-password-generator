from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    # return HttpResponse("Hello this is main page")
    return render(request, "generator/home.html")


def password(request):
    thepassword = ""
    length = int(request.GET.get("Length", 8))
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend("0123456789")
    if request.GET.get("special"):
        characters.extend("!@#$%^&*")

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})


def about(request):
    return render(request, "generator/about.html")

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.http import HttpRequest

from datetime import date
import datetime

def index(request : HttpRequest):
    return render(request, "pages/index.html", {
        "segment" : "index", 
    })
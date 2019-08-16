from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# dashboard landing page
def dashboard(Request):
    return HttpResponse("Hey ya")


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def checkouts(request):
    return HttpResponse("Checkouts endpoint working")
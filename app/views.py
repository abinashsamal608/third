from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string_response(request):
    return HttpResponse ('This is my first string')

def second_response(request):
    return HttpResponse ('Second response of the day')

def third_response(request):
    return HttpResponse ('Third response created by me')
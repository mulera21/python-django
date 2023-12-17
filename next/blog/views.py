from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Blog home</h1>")

def nice(request):
    return HttpResponse("<h1>service</h1>")

def fly(request):
    return HttpResponse("<h1> contact </h1>")
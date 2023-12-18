from django.shortcuts import render


def home(request):
    return render(request, "web/home.html")

def nice(request):
    return render(request, "web/about.html")

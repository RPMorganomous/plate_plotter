from django.shortcuts import render


def index(request):
    return render(request, 'plot/index.html')


def profile(request):
    return render(request, 'plot/profile.html')

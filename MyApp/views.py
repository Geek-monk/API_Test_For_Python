# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    print('流年莫虚掷，华发不相容')
    return render(request, "welcome.html")

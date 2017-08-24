from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    elements = {
        'message': 'Hey You! Welcome to your very first Django app. I hope you are having fun!',
        'id': 2345,
    }
    return render(request, "main/home.html", elements)

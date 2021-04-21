from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome_view(request):
    print('This line is printed by view function while processing request')
    print(10/0)
    return HttpResponse('<h1>Custum Middleware Demo</h1>')

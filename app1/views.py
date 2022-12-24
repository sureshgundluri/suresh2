from django.shortcuts import render
from django.http import HttpResponse
def first(request):
    return  HttpResponse('this is my first view')
def suresh(request):
    return HttpResponse('Happy christmas')

# Create your views here.

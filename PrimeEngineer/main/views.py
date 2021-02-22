from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("This is my very first home page in <strong> Django</strong> wow!!")

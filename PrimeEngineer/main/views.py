from django.shortcuts import render
from django.http import HttpResponse
#from .models import Works
from .models import Works
# Create your views here.
def HomePage(request):
    return render(request=request,
                   template_name="main/home.html",
                   context={"works": Works.objects.all})

def Head(request):
    return render(request=request,
                   template_name="/main/templates/header.html")

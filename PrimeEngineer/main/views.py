from django.shortcuts import render
from django.http import HttpResponse
from .models import Works
# Create your views here.
def homepage(request):
    return render( request = request,
                   template_name = "main/template/main/home.html",
                   context={"works": Works.objects.all})

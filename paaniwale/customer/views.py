from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'paaniwale/base.html')
def details(request):
    return render(request,'paaniwale/details.html')

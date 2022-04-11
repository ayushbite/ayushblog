
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("hola worlda")

def post(request):
    pass

def postdetail(request):
    pass

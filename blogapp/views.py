
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,"/blo")

def post(request):
    pass

def postdetail(request):
    pass

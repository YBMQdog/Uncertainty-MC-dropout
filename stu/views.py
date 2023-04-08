from PIL.Image import Image
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return  HttpResponse('hello world!')

def test(request):
    return HttpResponse('good evening!')


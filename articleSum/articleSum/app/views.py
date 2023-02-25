from django.shortcuts import render
from django.http import HttpResponse
from .key import API_KEY
import openai
# Create your views here.
def home(request):
    return (
        render(request,'base.html')
    )

def error_handler(request):
    return HttpResponse('404 Page')
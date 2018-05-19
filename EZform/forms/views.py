from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'forms/index.html')

def form(request):
    return render(request, 'forms/form.html')

    
'''
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the form index.")

def form(request):
    return HttpResponse("Hello, world. You're at the form sub-form index.")
'''
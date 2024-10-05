from django.shortcuts import render,HttpResponse

# Create your views here.

def firstView(request):
    return HttpResponse('welcome to first page')

def secondView(request):
    return HttpResponse('welcome to second page')
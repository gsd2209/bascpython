from django.shortcuts import render,HttpResponse

# Create your views here.
def thirdView(request):
    return HttpResponse('welcome to third page')

def fourthView(request):
    return HttpResponse('welcome to fourth page')
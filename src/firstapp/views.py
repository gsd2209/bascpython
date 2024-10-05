from django.shortcuts import render

# Create your views here.

def firstView(request):
    return render(request,'first.html')

def secondView(request):
    return render(request,'second.html')
from django.shortcuts import render

# Create your views here.
def thirdView(request):
    return render(request,'fourth.html')

def fourthView(request):
    return render(request,'third.html')
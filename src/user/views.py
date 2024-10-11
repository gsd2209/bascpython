from django.shortcuts import render
from .models import User

# Create your views here.
def createUser(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        city=request.POST.get('city')
        password=request.POST.get('password')
        email=request.POST.get('email')
        print(name,email,city,password)
        user=User()
        user.name=name
        user.city=city
        user.email=email
        user.password=password
        user.save()

    return render (request,'createuser.html')

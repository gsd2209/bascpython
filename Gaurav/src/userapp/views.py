from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def indexView(request):
    return render(request,'index.html')

def createUser(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User(name=name,city=city,password=password,email=email)
        user.save()
        return redirect('/')
    return render(request,'userform.html')

def allUsers(request):
    name='karan'
    users=User.objects.all()
    return render(request,'userlist.html',{'name':name,'users':users})

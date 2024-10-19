from django.shortcuts import render,redirect
from .models import User,Blogs

# Create your views here.
def indexView(request):
    title='abc'
    description='nothing'
    Blogs(title=title,description=description).save()
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
    users=User.objects.all()
    return render(request,'userlist.html',{'users':users})

def viewUser(request,id):
    user=User.objects.get(id=id)
    return render(request,'user.html',{'user':user})

def editUser(request,id):
    user=User.objects.get(id=id)
    if(request.method=='POST'):
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user.name=name
        user.city=city
        user.email=email
        user.password=password
        user.save()
        return redirect('/crud/allUsers')
    return render(request,'editform.html',{'user':user})

def deleteUser(request,id):
    User.objects.get(id=id).delete()
    return redirect('/crud/allUsers') 
from django.shortcuts import render

# Create your views here.
def createUser(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        city=request.POST.get('city')
        password=request.POST.get('password')
        email=request.POST.get('email')
        print(name,email,city,password)
    return render (request,'createuser.html')

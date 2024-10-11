from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        return redirect('/login')
    return render(request,'register.html')

def loginView(request):
    return render(request,'login.html')
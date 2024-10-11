
from django.contrib import admin
from django.urls import path,include
from myauth import views as authview



urlpatterns = [
    path('',authview.index),
    path('admin/', admin.site.urls),
    path('login',authview.loginView),
    path('user/',include('user.urls'))
    
]

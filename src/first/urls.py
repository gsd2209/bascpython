
from django.contrib import admin
from django.urls import path,include
from firstapp import views as v


urlpatterns = [
    path('',v.index),
    path('admin/', admin.site.urls),
    path('firstapp/',include('firstapp.urls')),
    path('secondapp/',include('secondapp.urls'))
]

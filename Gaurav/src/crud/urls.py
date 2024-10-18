
from django.contrib import admin
from django.urls import path,include
from userapp.views import indexView

urlpatterns = [
    path('',indexView),
    path('admin/', admin.site.urls),
    path('crud/',include('userapp.urls'))
]
    
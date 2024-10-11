
from django.urls import path
from . import views as v


urlpatterns = [
    
    path('first-url',v.firstView),
    path('second-url',v.secondView),
]
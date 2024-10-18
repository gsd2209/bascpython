from django.urls import path
from .import views as v
urlpatterns=[
    path('createUser',v.createUser),
    path('allUsers',v.allUsers)
]
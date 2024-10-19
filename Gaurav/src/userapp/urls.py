from django.urls import path
from .import views as v
urlpatterns=[
    path('createUser',v.createUser),
    path('allUsers',v.allUsers),
    path('viewUser/<int:id>',v.viewUser),
    path('editUser/<int:id>',v.editUser),
    path('deleteUser/<int:id>',v.deleteUser)
]
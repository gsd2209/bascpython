from django.urls import path
from . import views as v


urlpatterns = [
    
    path('third-url',v.thirdView),
    path('fourth-url',v.fourthView)
]
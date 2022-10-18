#URLs of app -

from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
    path('version', views.version),
   
]

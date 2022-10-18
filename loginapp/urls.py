#urls for login app

from django.urls import path
from .import views

urlpatterns = [
    path('login',views.login),
    path('logintask',views.logintask),
    path('Regi',views.Regi),
    path('insert',views.insert),
    path('msg',views.msg),
    ]

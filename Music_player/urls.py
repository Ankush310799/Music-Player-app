#URL of Music_playerc -

from django.urls import path,include
from .import views
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    
    
    
    
    path('music/', include('app.urls',)),
    path('', include('loginapp.urls',)),
    
]

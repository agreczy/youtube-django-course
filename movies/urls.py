from django.contrib import admin
from django.urls import path
from movies import viewes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', viewes.movies), 
    path('', viewes.home)
]

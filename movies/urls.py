from django.contrib import admin
from django.urls import path
from movies import viewes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', viewes.movies), 
    path('', viewes.home),
    path('movies/<int:id>', viewes.detail),
    path('movies/add', viewes.add),
    path('movies/delete/<int:id>', viewes.delete) 
]
 
from django.http import HttpResponse
from django.shortcuts import render

movieData = {
    'movies': [
        {
            'id': 5,
            'title': 'Jaws',
            'year': 1996
        },
        {
            'id': 6,
            'title': 'Fight club',
            'year': 1999
        },
        {
            'id': 7,
            'title': 'Mr. Robot',
            'year': 2018
        }
    ]
}

def movies(request) :
    return render(request, 'movies/movies.html', movieData)

def home(request) :
    return HttpResponse("Home page")

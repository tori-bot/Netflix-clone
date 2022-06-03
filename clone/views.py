from django.shortcuts import render
from .requests import get_all_movies,one_movie,youtube_trailer,search


# Create your views here.
def home(request):
    title='Netflix'
    movies=get_all_movies('popular')


    context={
        'title':title,
        'movies':movies,
    }

    return render(request,'index.html',context)

def movie(request,movie_id):
    movie=one_movie(movie_id)
    youtube_id=youtube_trailer(movie['title'] )
    trailer_url=f'https://www.youtube.com/embed/{youtube_id}?autoplay=1&muted=0'

    
    
    context={
        'movie':movie,
        'trailer_url':trailer_url,
    }

    return render(request,'one_movie.html',context)

def search(request,title):
    movies=search(title)

    context={
        'movies':movies,
    }
    return render(request,'search.html',context)


# <iframe width="560" height="315" src="{{trailer_url}}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
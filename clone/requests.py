 import requests
from decouple import config

def get_all_movies(category):
    
    url=f'https://api.themoviedb.org/3/movie/{category}?api_key={config("API_KEY")}'
    response=requests.get(url)
    movies=response.json()
    movie_list=[]
    for item in movies['results']:
        if item['poster_path'] is not None:
            movie_list.append(item)
    return movie_list

def one_movie(movie_id):
    url=f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={config("API_KEY")}'
    response=requests.get(url)
    movie=response.json()
    return movie

def youtube_trailer(title):
    search_query = title.replace(' ', '+')
    url=f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={search_query}&key={config("YOUTUBE_API")}'
    response=requests.get(url)
    youtube_id = response.json()['items'][0]['id']['videoId']
    return youtube_id

def search(title):
    search_query = title.replace(' ', '+')
    url=f'https://api.themoviedb.org/3/search/movie?api_key={config("API_KEY")}&query={search_query}'
    response=requests.get(url)
    movies=response.json()
    search_results=[]
    for item in movies['results']:
        if item['poster_path'] is not None:
            search_results.append(item)
    return search_results

    
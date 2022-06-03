from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('details/<int:movie_id>', views.movie,name='details'),
    path('search/',views.search,name='search')
]

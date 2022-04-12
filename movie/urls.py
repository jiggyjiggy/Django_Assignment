from django.urls import path
from movie.views import ActorCreateView, MovieCreateView, ActorMovieConnetionView
from movie.views import ActorReadView, MovieReadView

urlpatterns = [
    path('actors/', ActorCreateView.as_view()),
    path('movies/', MovieCreateView.as_view()),
    path('actormovie/', ActorMovieConnetionView.as_view()),
    path('actorInfo/', ActorReadView.as_view()),
    path('movieInfo/', MovieReadView.as_view())
]
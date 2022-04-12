# from django.shortcuts import render

# Create your views here.

import json
from turtle import title 

from django.http import JsonResponse
from django.views import View

from movie.models import Actor, Movie, ActorMovie


# Create
class ActorCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(first_name=data['first_name'], last_name=data['last_name'], date_of_birth=data['date_of_birth'])
        return JsonResponse({'message' : 'created'}, status=201)  

class MovieCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(title=data['title'], release_date=data['release_date'], running_time=data['running_time'])
        return JsonResponse({'message' : 'created'}, status=201)

class ActorMovieConnetionView(View):
    def post(self, request):
        data = json.loads(request.body) 
        first_name = Actor.objects.get(first_name=data['first_name'])
        title = Movie.objects.get(title=data['title'])
        ActorMovie.objects.create(actor=first_name, movie=title)
        return JsonResponse({'message' : 'created'}, status=201)


# Read
class ActorReadView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results=[]
        for actor in actors:
            movies_id = actor.actormovie_set.all()
            moviesList = []

            for movie in movies_id:
                moviesList.append(
                    {
                        'movie_title' : movie.movie.title
                    }
                )

            results.append(
                {
                    'actor_first_name' : actor.first_name,
                    'actor_last_name' : actor.last_name,
                    'movie' : moviesList
                }
            )

        return JsonResponse({'results' : results}, status=200)

class MovieReadView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results=[]

        for movie in movies:
            actors_id = movie.actormovie_set.all()
            actorsList = []

            for actor in actors_id:
                actorsList.append(
                    {
                        'actor_first_name' : actor.actor.first_name
                    }
                )
            
            results.append(
                {
                    'actor' : actorsList,
                    'movie_title' : movie.title,
                    'movie_running_time' : movie.running_time
                }
            )



        return JsonResponse({'results' : results}, status=200)

# from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

# Create
class OwnerCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data['name'], email=data['email'], age=data['age'])
        return JsonResponse({'message' : 'created'}, status=201)


class DogCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner=Owner.objects.get(name=data['owner'])
        Dog.objects.create(name=data['name'], age=data['age'], owner=owner)
        return JsonResponse({'message' : 'created'}, status=201)

# Info
class OwnerInfoView(View):
    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            results.append(
                {
                    'owners_name' : owner.name,
                    'owners_email' : owner.email,
                    'owners_age' : owner.age
                }
            )
       
        return JsonResponse({'results' : results}, status=200)     
    
class DogInfoView(View):
    def get(self, request):
        dogs = Dog.objects.all()

        results = []

        for dog in dogs:
            results.append(
                {
                    'dog_name' : dog.name,
                    'dog_age' : dog.age,
                    'owner_name' : dog.owner.name
                }
            )

        return JsonResponse({'results' : results}, status=200)   

class OwnerDogInfoView(View):
    def get(self, request):
        owners = Owner.objects.all()
        
        results = []

        for owner in owners: 
            dogs = owner.dog_set.all()
            dogslist = []

            for dog in dogs:
                dogslist.append(
                    {
                        'dog_name' : dog.name,
                        'dog_age' : dog.age
                    }
                )

            results.append(
                {
                    'owner_name' : owner.name,
                    'owners_email' : owner.email,
                    'owners_age' : owner.age,
                    'dog' : dogslist
                }
            )

        return JsonResponse({'results' : results}, status=200)  
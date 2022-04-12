from django.urls import path

from owners.views import DogCreateView, DogInfoView, OwnerCreateView, OwnerInfoView, OwnerDogInfoView


urlpatterns = [
    # Create
    path('/ownersCreate', OwnerCreateView.as_view()),
    path('/dogsCreate', DogCreateView.as_view()),

    # Info
    path('/ownersInfo', OwnerInfoView.as_view()),
    path('/ownersdogsInfo', OwnerDogInfoView.as_view()),
    path('/dogsInfo', DogInfoView.as_view())
]
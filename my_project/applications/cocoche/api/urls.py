from django.urls import path
from applications.cocoche.api.api_views import *

urlpatterns = [
    # Cocoche APIs:
    path('get_cars/list', GetCarsListAPIView.as_view()),
    path('get_ford_cars', GetFordCarsAPIView.as_view()),
    path('create_user', CreateUserAPIView.as_view()),
]
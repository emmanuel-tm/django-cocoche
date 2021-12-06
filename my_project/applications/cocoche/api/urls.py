from django.urls import path
from applications.cocoche.api.cocoche_api_views import *
from applications.cocoche.api.api_views import *

urlpatterns = [
    # Cocoche APIs:
    path('get_cars/', get_cars),
    path('get_cars/list', GetCarsListAPIView.as_view())
]
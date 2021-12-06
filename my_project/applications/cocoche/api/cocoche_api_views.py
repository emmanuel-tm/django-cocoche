from django.db.models import query
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import json

from applications.cocoche.models import CarsList


# NOTE: We declare the variables related to the Cocoche API.
URL_BASE = 'https://server.cocoche.com.ar'
ENDPOINT = '/car_listing_presentation'
PARAMS = dict(list_length=100)


@api_view(['GET'])
@permission_classes([]) # NOTE: No type of permission is required
def get_cars(request):

    url = URL_BASE + ENDPOINT
    payload = PARAMS
    
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        cars = json.loads(response.text)
        cars_list = cars.get('carList')

        i = 0
        
        for car in cars_list:
            owner_id = car.get('ownerId')
            car_id = car.get('carId')
            title = car.get('title')
            doors = car.get('doors')
            cost = car.get('cost')
            url = car.get('url')
            fuel_type = car.get('fuelType')
            description = car.get('description')
            model_description = car.get('modelDescription')
            brand_description = car.get('brandDescription')
            place_description = car.get('placeDescription')
            latitude = car.get('latitude')
            longitude = car.get('longitude')
            location = car.get('location')
            califications_avg = car.get('calificationsAvg')
            currency = car.get('currency')
            year = car.get('year')
            rents_qty = car.get('rentsQuantity')

            try:
                car = CarsList.objects.get(owner_id=owner_id, car_id=car_id)
                queryset = CarsList.objects.filter(owner_id=owner_id, car_id=car_id)
                queryset.update(
                    title = title,
                    doors = doors,
                    cost = cost,
                    url = url,
                    fuel_type = fuel_type,
                    description = description,
                    model_description = model_description,
                    brand_description = brand_description,
                    place_description = place_description,
                    latitude = latitude,
                    longitude = longitude,
                    location = location,
                    califications_avg = califications_avg,
                    currency = currency,
                    year = year,
                    rents_qty = rents_qty
                )
            
            except CarsList.DoesNotExist:
                # NOTE: If does not exist, we create a new one.
                item = CarsList.objects.create(
                    owner_id = owner_id,
                    car_id = car_id,
                    title = title,
                    doors = doors,
                    cost = cost,
                    url = url,
                    fuel_type = fuel_type,
                    description = description,
                    model_description = model_description,
                    brand_description = brand_description,
                    place_description = place_description,
                    latitude = latitude,
                    longitude = longitude,
                    location = location,
                    califications_avg = califications_avg,
                    currency = currency,
                    year = year,
                    rents_qty = rents_qty
                )
                item.save()
                i += 1
                print(i)

        return HttpResponse('<h1>Updated Database.</h1>')
    else:
        return HttpResponse('<h1>Error in the Database.</h1>')
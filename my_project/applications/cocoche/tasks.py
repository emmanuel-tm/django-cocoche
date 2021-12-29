# Import the libraries:
from celery import shared_task
from applications.cocoche.models import CarsList

import requests
import json

# NOTE: We declare the variables related to Cocoche API.
URL_BASE = 'https://server.cocoche.com.ar'
ENDPOINT = '/car_listing_presentation'
PARAMS = dict(list_length=100)

# Create your tasks here:
@shared_task
def get_cars():
    '''
    \nFunción que actúa como tarea asincrónica para obtener la lista
    \nde los autos y sus detalles, en caso de existir se actualiza el
    \nauto en la base de datos, de lo contrario, se registra como uno nuevo.
    '''

    url = URL_BASE + ENDPOINT
    payload = PARAMS
    
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        cars = json.loads(response.text)
        cars_list = cars.get('carList')

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
                # NOTE: Update car object
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

        print('{"code": 200, "message": "updated database"}')
    else:
        print('{"code": 500, "message": internal server error"}')
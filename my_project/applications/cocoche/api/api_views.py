from typing import List

from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.settings import perform_import
# NOTE: import my serializers and my models.
from applications.cocoche.api.serializers import *
from applications.cocoche.models import *

from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView


class GetCarsListAPIView (ListAPIView):
    '''
    [METODO HTTP: GET]
    \nEsta vista de API genérica devuelve una lista de todos
    \nlos autos presentes en la base de datos.
    '''
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializer
    permission_classes = []

class GetFordCarsAPIView(ListAPIView):
    '''
    [METODO HTTP: GET]
    \nEsta vista de API genérica-personalizada devuelve una lista
    \nde todos los autos presentes en la base de datos cuya marca 
    \nes "FORD".
    '''
    serializer_class = CarsListSerializer
    permission_classes = []

    def get_queryset(self):
        '''
        Sobreescribimos el método "get_queryset()" para poder filtrar
        aquellos autos cuya marca es "FORD".
        '''
        try:
            queryset = CarsList.objects.filter(brand_description='FORD')
            return queryset
        except Exception as error:
            return {'error': f'Ha ocurrido el siguiente error: {error}'}
from typing import List

from rest_framework import permissions
# NOTE: import my serializers and my models.
from applications.cocoche.api.serializers import *
from applications.cocoche.models import *

from rest_framework.permissions import IsAdminUser

from rest_framework.generics import ListAPIView


class GetCarsListAPIView (ListAPIView):
    '''
    [METODO GET]
    Esta vista de API genérica devuelve una lista de todos
    los autos presentes en la base de datos.
    '''
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializer
    permission_classes = []

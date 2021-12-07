# NOTE: import my serializers and my models.
from django.http import response
from applications.cocoche.api.serializers import *
from applications.cocoche.models import *

from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

import hashlib
from datetime import datetime


class GetCarsListAPIView (ListAPIView):
    __doc__ = '''
    [METODO HTTP: GET]
    \nEsta vista de API genérica devuelve una lista de todos
    \nlos autos presentes en la base de datos.
    '''
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializer
    permission_classes = []


class GetFordCarsAPIView(ListAPIView):
    __doc__ = '''
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


class CreateUserAPIView(APIView):
    '''
    [METODO HTTP: POST]
    \nVista de API Genérica-Personalizada basadas en Clases que
    \n recibe peticiones de tipo "POST".
    \nSchema:
    \n{
    \n  "name": "string", 
    \n  "phone": "string", 
    \n  "email": "string"
    \n}
    '''

    permission_classes = []
    authentication_classes = []
    parser_classes = [JSONParser]
    
    def post(self, request, format=None):
        '''
        Se sobreescribe la función asociada al método POST para 
        \nque reciba mediante el "request" los datos enviados.
        \n`Content-Type: 'application/json`.
        \n`Schema:`
        \n`{`
        \n` "name": "Emmanuel",`
        \n` "phone": "1234567899",`
        \n` "email": "email3456@gmail.com"`
        \n`}`
        '''

        user_data = {}

        # NOTE:I get the parameters that arrive by METHOD HTTP: POST.
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')

        serializer = UserSerializer(data=request.data)

        try:
            # Get User
            user = User.objects.get(email=email)

        # NOTE: If does not exist enter:
        except User.DoesNotExist:
            try:
                random_id = hashlib.md5(email.encode()).hexdigest()
                today = datetime.now()
                today_str = today.strftime('%d-%m-%Y')

            # NOTE: In case an exception ocurrs: for example: "No parameter is entered"
            except Exception as error:
                user_data = {'code': 500, 'message': 'missing data'}
                return Response(data=user_data)

            if serializer.is_valid() and type(phone) == str and phone.isdigit() and type(name) == str:
                # Create a new User object:
                user = User.objects.create(
                    name = name,
                    phone = phone,
                    email = email,
                    random_id = random_id,
                    createAt = today_str
                )

                user.save()

                user_data['id'] = user.random_id
                user_data['createAt'] = user.createAt
                return Response(data=user_data)

            else:
                user_data = {'code': 500, 'message': 'data wrongly entered'}
                return Response(data=user_data)

        except Exception as error:
            user_data = {'code': 500, 'message': f'{error}'}
            return Response(data=user_data)
        
        user_data = {'code': 500, 'message': 'email already registered'}
        return Response(data=user_data)
from django.db.models import fields
# Import serializers and my Models
from rest_framework import serializers
from applications.cocoche.models import CarsList, User

# NOTE: List of serializers:
class CarsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarsList
        fields = ('owner_id', 'car_id', 'title', 'doors',
                    'cost', 'url', 'fuel_type', 'decription',
                    'model_description', 'brand_description',
                    'place_description', 'latitude', 'longitude',
                    'location', 'califications_avg', 'currency',
                    'year', 'rents_qty')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('__all__')
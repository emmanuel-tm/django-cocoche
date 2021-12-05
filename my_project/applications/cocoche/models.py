from django.db import models
from django.db.models.fields import BigAutoField, CharField, PositiveIntegerField, PositiveSmallIntegerField

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name = models.CharField(verbose_name='name', max_length=120, default='')
    phone = models.CharField(verbose_name='phone', max_length=30, default='0000000000')
    email = models.EmailField(verbose_name='email', unique=True)
    random_id = models.CharField(verbose_name='random id', max_length=100, unique=True)
    createAt = models.CharField(verbose_name='create at', max_length=10, default='dd-mm-AAAA')

    class Meta:
        db_table = 'cocoche_users'

    def __str__(self):
        return f'{self.id}'


class CarsList (models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    owner_id = models.CharField(verbose_name='owner id', max_length=120, unique=True)
    car_id = models.CharField(verbose_name='car id', max_length=120, unique=True)
    doors = models.PositiveSmallIntegerField(verbose_name='doors', default=0)
    cost = models.PositiveIntegerField(verbose_name='cost', default=0)
    url = models.CharField(verbose_name='url', max_length=150, default='')
    fuel_type = models.CharField(verbose_name='fuel type', max_length=50, default='')
    description = models.TextField(verbose_name='description', default='')
    model_description = models.CharField(verbose_name='model description', max_length=150, default='')
    place_description = models.CharField(verbose_name='place description', max_length=150, default='')
    latitude = models.CharField(verbose_name='latitude', max_length=50, default='')
    longitude = models.CharField(verbose_name='longitude', max_length=50, default='')
    location = models.CharField(verbose_name='location', max_length=150, default='')
    califications_avg = models.FloatField(verbose_name='califications avg', default=0.0)
    currency = models.CharField(verbose_name='currency', max_length=50, default='ARS')
    year = models.PositiveSmallIntegerField(verbose_name='year', default=0)
    rents_qty = models.IntegerField(verbose_name='rents quantity', default=0)

    class Meta:
        db_table = 'cocoche_cars_list'

    def __str__(self):
        return f'{self.id}'


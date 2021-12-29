# Generated by Django 3.2.2 on 2021-12-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocoche', '0002_auto_20211205_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarsList',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('owner_id', models.CharField(max_length=120, unique=True, verbose_name='owner id')),
                ('car_id', models.CharField(max_length=120, unique=True, verbose_name='car id')),
                ('doors', models.PositiveSmallIntegerField(default=0, verbose_name='doors')),
                ('cost', models.PositiveIntegerField(default=0, verbose_name='cost')),
                ('url', models.CharField(default='', max_length=150, verbose_name='url')),
                ('fuel_type', models.CharField(default='', max_length=50, verbose_name='fuel type')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('model_description', models.CharField(default='', max_length=150, verbose_name='model description')),
                ('place_description', models.CharField(default='', max_length=150, verbose_name='place description')),
                ('latitude', models.CharField(default='', max_length=50, verbose_name='latitude')),
                ('longitude', models.CharField(default='', max_length=50, verbose_name='longitude')),
                ('location', models.CharField(default='', max_length=150, verbose_name='location')),
                ('califications_avg', models.FloatField(default=0.0, verbose_name='califications avg')),
                ('currency', models.CharField(default='ARS', max_length=50, verbose_name='currency')),
                ('year', models.PositiveSmallIntegerField(default=0, verbose_name='year')),
                ('rents_qty', models.IntegerField(default=0, verbose_name='rents quantity')),
            ],
            options={
                'db_table': 'cocoche_cars_list',
            },
        ),
    ]

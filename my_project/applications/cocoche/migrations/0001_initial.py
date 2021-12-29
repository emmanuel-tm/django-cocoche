# Generated by Django 3.2.2 on 2021-12-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=120, verbose_name='titles')),
                ('phone', models.CharField(default='0000000000', max_length=30, verbose_name='phones')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='emails')),
                ('random_id', models.CharField(max_length=100, unique=True, verbose_name='random ids')),
                ('createAt', models.CharField(default='dd-mm-AAAA', max_length=10, verbose_name='create at')),
            ],
            options={
                'db_table': 'cocoche_users',
            },
        ),
    ]

from django.db import models

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

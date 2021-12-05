from django.contrib import admin

# Import my models:
from applications.cocoche.models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


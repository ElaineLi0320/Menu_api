from django.contrib import admin
from .models import Appetizer
from .models import MainCourse
from .models import Dessert
from .models import Drink

# Registering the models with Django's admin interface.
admin.site.register(Appetizer)
admin.site.register(MainCourse)
admin.site.register(Dessert)
admin.site.register(Drink)

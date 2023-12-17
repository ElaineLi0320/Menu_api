"""
Transform a python object to JSON
"""
from rest_framework import serializers
from .models import Appetizer
from .models import MainCourse
from .models import Dessert
from .models import Drink


class AppetizerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Appetizer model.
    """
    class Meta:
        model = Appetizer
        fields = ['id', 'name', 'description']


class MainCourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the MainCourse model.
    """
    class Meta:
        model = MainCourse
        fields = ['id', 'name', 'description']


class DessertSerializer(serializers.ModelSerializer):
    """
    Serializer for the Dessert model.
    """
    class Meta:
        model = Dessert
        fields = ['id', 'name', 'description']


class DrinkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Drink model.

    Attributes:
        Meta: An inner class that defines metadata for the DrinkSerializer class.
              It specifies the model to be serialized (Drink) and the fields of the
              model that should be included in the serialized data ('id', 'name',
              'description').
    """
    class Meta:
        """
        Meta class for DrinkSerializer.
        """
        model = Drink
        fields = ['id', 'name', 'description']

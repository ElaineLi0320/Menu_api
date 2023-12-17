"""
Create endpoints for drinks
"""
from ..models import Drink
from ..serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    """
    API endpoint for listing and creating drinks.
    Handles GET and POST requests. GET requests return a list of all drinks, while
    POST requests add a new drink to the database.

    Args:
        request: The HTTP request object.
        format: The format of the request (optional, defaults to None).

    Returns:
        Response: A Response object containing serialized drink data for GET requests,
                  or the new drink data for POST requests.
    """
    if request.method == 'GET':
        # Get all the drinks, serialize them and return JSON
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Deserialize the data then create a python object
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    """
    API endpoint for retrieving, updating, or deleting a specific drink.
    Handles GET, PUT, and DELETE requests. GET requests return data for a specific drink,
    PUT requests update a drink, and DELETE requests remove a drink from the database.

    Args:
        request: The HTTP request object.
        id: The primary key of the drink to be retrieved, updated, or deleted.
        format: The format of the request (optional, defaults to None).

    Returns:
        Response: A Response object containing the drink data for GET requests, updated
                  drink data for PUT requests, or a status code for DELETE requests.
    """
    # Get objects with primary keys
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

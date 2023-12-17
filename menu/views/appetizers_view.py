"""
Create endpoints for appetizers
"""
from ..models import Appetizer
from ..serializers import AppetizerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def appetizer_list(request, format=None):
    """
    API endpoint for listing and creating appetizers.

    Args:
        request: The HTTP request object.
        format: An optional string to specify the format of the response (default is None).

    Returns:
        Response: A Django REST framework Response object.
                  For GET requests, it contains serialized data of all appetizers.
                  For POST requests, it contains the serialized data of the newly created appetizer.
    """
    if request.method == 'GET':
        # Get all the drinks, serialize them and return JSON
        appetizers = Appetizer.objects.all()
        serializer = AppetizerSerializer(appetizers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Deserialize the data then create a python object
        serializer = AppetizerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def appetizer_detail(request, id, format=None):
    """
    API endpoint for retrieving, updating, or deleting a specific appetizer.

    Args:
        request: The HTTP request object.
        id: The primary key of the appetizer to be retrieved, updated, or deleted.
        format: An optional string to specify the format of the response (default is None).

    Returns:
        Response: A Django REST framework Response object.
                  For GET requests, it contains serialized data of the specified appetizer.
                  For PUT requests, it contains the updated data of the appetizer.
                  For DELETE requests, it returns a status code indicating the outcome of the deletion.
    """
    # Get objects with primary keys
    try:
        appetizer = Appetizer.objects.get(pk=id)
    except Appetizer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppetizerSerializer(appetizer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AppetizerSerializer(appetizer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        appetizer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

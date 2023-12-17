"""
Create endpoints for main courses
"""
from ..models import MainCourse
from ..serializers import MainCourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def main_course_list(request, format=None):
    """
    API endpoint for listing and creating main course items.

    Args:
        request: The HTTP request object.
        format: An optional string to specify the format of the response (default is None).

    Returns:
        Response: A Django REST framework Response object.
                  For GET requests, it contains serialized data of all main courses.
                  For POST requests, it contains the serialized data of the newly created main course item.
    """
    if request.method == 'GET':
        # Get all the drinks, serialize them and return JSON
        main_courses = MainCourse.objects.all()
        serializer = MainCourseSerializer(main_courses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Deserialize the data then create a python object
        serializer = MainCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def main_course_detail(request, id, format=None):
    """
    API endpoint for retrieving, updating, or deleting a specific main course item.

    Args:
        request: The HTTP request object.
        id: The primary key of the main course item to be retrieved, updated, or deleted.
        format: An optional string to specify the format of the response (default is None).

    Returns:
        Response: A Django REST framework Response object.
                  For GET requests, it contains serialized data of the specified main course item.
                  For PUT requests, it contains the updated data of the main course item.
                  For DELETE requests, it returns a status code indicating the outcome of the deletion.
    """
    # Get objects with primary keys
    try:
        main_course = MainCourse.objects.get(pk=id)
    except MainCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MainCourseSerializer(main_course)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MainCourseSerializer(main_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        main_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

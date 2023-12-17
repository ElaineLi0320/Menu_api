"""menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import appetizers_view, main_courses_view, desserts_view, drinks_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appetizers/', appetizers_view.appetizer_list),
    path('appetizers/<int:id>', appetizers_view.appetizer_detail),
    path('main_courses/', main_courses_view.main_course_list),
    path('main_courses/<int:id>', main_courses_view. main_course_detail),
    path('desserts/', desserts_view.dessert_list),
    path('desserts/<int:id>', desserts_view.dessert_detail),
    path('drinks/', drinks_view.drink_list),
    path('drinks/<int:id>', drinks_view.drink_detail)
]

# Get JSON through browser
urlpatterns = format_suffix_patterns(urlpatterns)
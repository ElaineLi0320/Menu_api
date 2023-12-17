from django.db import models


class Appetizer(models.Model):
    """
    Represents an appetizer, including its name and description.

    Attributes:
        name (models.CharField): The name of the appetizer.
        description (models.CharField): A brief description of the appetizer.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        """
        Returns a string representation of the appetizer, which is its name.

        Returns:
            str: The name of the appetizer.
        """
        return self.name


class MainCourse(models.Model):
    """
    Represents a main course item in the restaurant menu.

    This model stores information about each main course, including its name and a brief description.

    Attributes:
        name (models.CharField): The name of the main course. This is a required field with a maximum length of 200 characters.
        description (models.CharField): A brief description of the main course. This field is also required and allows up to 500 characters.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        """
        Returns a string representation of the main course, which is its name.

        This method ensures that when an instance of MainCourse is printed or displayed, 
        it shows the name of the main course, making it easily identifiable.

        Returns:
            str: The name of the main course.
        """
        return self.name


class Dessert(models.Model):
    """
    Represents a dessert item in the restaurant menu.

    This model is used to store details about each dessert, including its name and a description. 
    It's part of the restaurant's menu management system, enabling easy maintenance and display of dessert options.

    Attributes:
        name (models.CharField): The name of the dessert. This field is required and can hold up to 200 characters.
        description (models.CharField): A brief description of the dessert. This field is also required and has a maximum length of 500 characters.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        """
        Returns a string representation of the dessert, which is its name.

        This method is primarily used in Django's admin interface and in debugging processes, where
        representing the object as its name improves readability and ease of identification.

        Returns:
            str: The name of the dessert.
        """
        return self.name


class Drink(models.Model):
    """
    Drink model representing a beverage with a name and description.

    Attributes:
        name (models.CharField): The name of the drink. This field is required and has a
                                 maximum length of 200 characters.
        description (models.CharField): A brief description of the drink. This field is required
                                       and has a maximum length of 500 characters.

    Methods:
        __str__(self): Returns a string representation of the Drink instance, which includes
                       both its name and description.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        """
        Return a string representation of the Drink instance.

        Returns:
            str: The name of the drink concatenated into a single string.
        """
        return self.name

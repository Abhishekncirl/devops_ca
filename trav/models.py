"""
Module for defining models.
"""
from django.db import models

class Trav(models.Model):   # pylint: disable=missing-class-docstring
    title = models.CharField(max_length=200)
    place_info =models.TextField()   # pylint: disable=trailing-whitespace
    best_time_to_visit =models.DateTimeField('best time to visit')  # pylint: disable=trailing-whitespace
    image_url = models.URLField(blank=True, null=True)   # pylint: disable=trailing-whitespace

    def __str__(self):
        return self.title + ""

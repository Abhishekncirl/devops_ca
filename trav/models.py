from django.db import models
class Trav(models.Model):
    """Creating models method"""
    title = models.CharField(max_length=200)
    place_info = models.TextField() 
    best_time_to_visit = models.DateTimeField('best time to visit') 
    image_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title + " "
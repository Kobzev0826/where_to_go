from django.db import models

class Place(models.Model):
    title = models.CharField('Title', max_length=100)
    short_description = models.TextField('Short description', blank=True)
    detail_description =  models.TextField("Detailed description", blank=True)
    lat = models.FloatField('Latitude')
    lon = models.FloatField('Longitude')

    def __str__(self):
        return self.title
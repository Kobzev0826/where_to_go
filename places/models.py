from django.db import models

class Place(models.Model):
    title = models.CharField('Title', max_length=100)
    short_description = models.TextField('Short description', blank=True)
    detail_description =  models.TextField("Detailed description", blank=True)
    lat = models.FloatField('Latitude')
    lon = models.FloatField('Longitude')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Image', upload_to='')
    place = models.ForeignKey(
        'Place', verbose_name='Place', related_name='images', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Position', default=0)
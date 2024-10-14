from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField('Title', max_length=100)
    short_description = models.TextField('Short description', blank=True)
    detail_description =  HTMLField("Detailed description", blank=True)
    lat = models.FloatField('Latitude')
    lon = models.FloatField('Longitude')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Image', upload_to='')
    place = models.ForeignKey(
        'Place', verbose_name='Place', related_name='images', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Position', default=0)

    @property
    def image_preview(self):
        if self.image:
            return format_html(
                mark_safe('<img src="{}" style="max-height:200px">'),
                self.image.url,
            )
        return ""

    class Meta(object):
        ordering = ['position']
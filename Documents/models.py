from django.db import models
from sorl.thumbnail import ImageField


class Documents(models.Model):
    title = models.CharField(max_length=20, verbose_name='title')
    image = ImageField(upload_to='media/Document_images')

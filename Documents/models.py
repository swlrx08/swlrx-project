from django.db import models


class Documents(models.Model):
    title = models.CharField(max_length=20, verbose_name='title')
    image = models.ImageField(upload_to='media/Document_images')

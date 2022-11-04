from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    shop_the_collection = models.CharField(max_length=256)
    slider_image = models.ImageField(upload_to='home-img/')

    def __str__(self):
        return self.title

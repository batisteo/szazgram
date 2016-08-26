from django.db import models


class Illustration(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title

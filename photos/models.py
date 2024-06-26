from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

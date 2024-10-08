from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    designation = models.CharField(max_length=255)
    facebook = models.URLField(default='')
    twitter = models.URLField(default='')
    instagram = models.URLField(default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
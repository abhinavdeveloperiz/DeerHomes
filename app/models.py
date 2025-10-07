from django.db import models

# Create your models here.

class BannerHome(models.Model):
    image1 = models.ImageField(upload_to='banners/')
    image2 = models.ImageField(upload_to='banners/')



class gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
    


class Project(models.Model):
    TYPE_CHOICES = [
        ('residential', 'Residences'),
        ('hotels', 'Hotels'),
        ('institutions', 'Institutions'),
        ('commercial', 'Commercial'),
        ('interiors', 'Interiors'),
        ('public_spaces', 'Public Spaces'),
        ('completed', 'Completed Projects'),
        ('upcoming', 'Upcoming Projects'),
    ]

    title = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    # Images
    image1 = models.ImageField(upload_to='projects/')
    image2 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image3 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image4 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image5 = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.client_name or 'No Client'}"



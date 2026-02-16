from django.db import models

# Create your models here.

class BannerHome(models.Model):
    image1 = models.ImageField(upload_to='banners/')
    image2 = models.ImageField(upload_to='banners/')




    


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

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.title} - {self.type or 'No Type'}"




class ServiceCategory(models.Model):
    image = models.ImageField(upload_to='service_categories/')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey( ServiceCategory, on_delete=models.CASCADE, related_name='services')

    image1 = models.ImageField(upload_to='service_images/')
    image2 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='service_images/', blank=True, null=True)

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title or f"Service ({self.category.name})"


class Blogs(models.Model):
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    photo = models.ImageField(upload_to='team_members/')

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    

class Directors(models.Model):
    photo = models.ImageField(upload_to='directors/')
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"

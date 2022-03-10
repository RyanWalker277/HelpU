from django.db import models

# Create your models here.

class places(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()

    
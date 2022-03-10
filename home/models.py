from django.db import models

# Create your models here.

class places(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()

class restraunts(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()

class libraries(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()

class toilets(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()

class malls(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()    

class hospitals(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()

class banks(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Location = models.TextField()
    Rating = models.FloatField()
    Image = models.URLField()
    Price = models.FloatField()
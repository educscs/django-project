from django.db import models
import uuid
# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Artist(models.Model):
    """Model representing an artist."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Album(models.Model):
    """Model representing an album."""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Song(models.Model):
    """Model representing a song."""
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album,on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    def __str__(self):
        """String for representing the Model object."""
        return self.title
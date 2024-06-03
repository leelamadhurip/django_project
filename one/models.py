# models.py
from django.db import models
from django.contrib.auth.models import User

class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_list = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    imdb_id = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    

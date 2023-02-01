from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.ManyToManyField(Genre)
    pages = models.IntegerField()

    def __str__(self):
        return self.name
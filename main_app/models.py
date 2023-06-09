from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publishers_detail', kwargs={'pk': self.id})

class Game(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    publisher = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'pk': self.id})

class Review(models.Model):
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),MaxValueValidator(10)
        ])
    review = models.TextField(max_length=250)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
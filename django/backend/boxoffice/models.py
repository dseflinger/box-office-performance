from django.db import models

class Theater(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Movie(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Sales(models.Model):
    theaterId = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
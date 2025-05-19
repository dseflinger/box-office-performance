from django.db import models

class Theater(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    num_screens = models.IntegerField()
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = "ACTION", "Action"
        COMEDY = "COMEDY", "Comedy"
        DRAMA = "DRAMA", "Drama"
        HORROR = "HORROR", "Horror"
        ROMANCE = "ROMANCE", "Romance"
        SCIFI = "SCIFI", "Sci-Fi"
        DOCUMENTARY = "DOC", "Documentary"

    name = models.CharField(max_length=100, null=False, blank=False)
    genre = models.CharField(max_length=10, choices=Genre.choices, default=Genre.ACTION)
    release_date = models.DateField()
    duration_minutes = models.IntegerField()

    def __str__(self):
        return self.name

class Sale(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    tickets_sold = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
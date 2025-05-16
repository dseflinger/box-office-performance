from datetime import date
from django.core.management.base import BaseCommand
from boxoffice.models import Sale, Theater, Movie


class Command(BaseCommand):
    help = "Loads initial sample data with theaters, movies, and sales"

    def handle(self, *args, **options):
        theater1 = Theater.objects.create(name="AMC Broadway", location="Santa Monica", num_screens=4, capacity=500)
        theater2 = Theater.objects.create(name="Cinemark 8", location="Van Nuys", num_screens=6, capacity=1000)
        theater3 = Theater.objects.create(name="Universal AMC", location="Studio City", num_screens=12, capacity=2000)

        movie1 = Movie.objects.create(name="Shrek", genre=Movie.Genre.COMEDY, release_date=date(2001, 5, 18), duration_minutes=89)
        movie2 = Movie.objects.create(name="Captain America", genre=Movie.Genre.ACTION, release_date=date(2025, 2, 14), duration_minutes=118)
        movie3 = Movie.objects.create(name="Final Destination", genre=Movie.Genre.HORROR, release_date=date(2025, 5, 16), duration_minutes=109)

        Sale.objects.create(theater=theater1, movie=movie1, date=date(2025, 5, 16), tickets_sold=150, amount=1800.00) 
        Sale.objects.create(theater=theater1, movie=movie1, date=date(2025, 5, 17), tickets_sold=200, amount=2400.00) 
        Sale.objects.create(theater=theater1, movie=movie2, date=date(2025, 5, 16), tickets_sold=163, amount=1956.00) 
        Sale.objects.create(theater=theater1, movie=movie2, date=date(2025, 5, 17), tickets_sold=150, amount=1800.00)
        Sale.objects.create(theater=theater1, movie=movie3, date=date(2025, 5, 16), tickets_sold=100, amount=1200.00) 
        Sale.objects.create(theater=theater1, movie=movie3, date=date(2025, 5, 17), tickets_sold=50, amount=600.00)

        Sale.objects.create(theater=theater2, movie=movie1, date=date(2025, 5, 16), tickets_sold=200, amount=1600.00) 
        Sale.objects.create(theater=theater2, movie=movie1, date=date(2025, 5, 17), tickets_sold=100, amount=800.00) 
        Sale.objects.create(theater=theater2, movie=movie2, date=date(2025, 5, 16), tickets_sold=250, amount=2000.00) 
        Sale.objects.create(theater=theater2, movie=movie2, date=date(2025, 5, 17), tickets_sold=300, amount=2400.00)
        Sale.objects.create(theater=theater2, movie=movie3, date=date(2025, 5, 16), tickets_sold=100, amount=800.00) 
        Sale.objects.create(theater=theater2, movie=movie3, date=date(2025, 5, 17), tickets_sold=50, amount=400.00)

        Sale.objects.create(theater=theater3, movie=movie1, date=date(2025, 5, 16), tickets_sold=200, amount=4000.00) 
        Sale.objects.create(theater=theater3, movie=movie1, date=date(2025, 5, 17), tickets_sold=100, amount=2000.00) 
        Sale.objects.create(theater=theater3, movie=movie2, date=date(2025, 5, 16), tickets_sold=250, amount=5000.00) 
        Sale.objects.create(theater=theater3, movie=movie2, date=date(2025, 5, 17), tickets_sold=300, amount=6000.00)
        Sale.objects.create(theater=theater3, movie=movie3, date=date(2025, 5, 16), tickets_sold=125, amount=2500.00) 
        Sale.objects.create(theater=theater3, movie=movie3, date=date(2025, 5, 17), tickets_sold=75, amount=1500.00)

        self.stdout.write(self.style.SUCCESS("Sample data loaded successfully."))

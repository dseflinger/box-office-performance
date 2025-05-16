from django.shortcuts import render
from boxoffice.models import Movie, Theater, Sale
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "boxoffice/home.html")

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, "boxoffice/movies.html", {"movies": movies})

def theaters_list(request):
    theaters = Theater.objects.all()
    return render(request, "boxoffice/theaters.html", {"theaters": theaters})

def sales_list(request):
    sales = Sale.objects.all()
    return render(request, "boxoffice/sales.html", {"sales": sales})

def revenue_summary(request):
    return HttpResponse("This is just a test")
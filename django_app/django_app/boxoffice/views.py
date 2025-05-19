from django.shortcuts import redirect, render
from boxoffice.models import Movie, Theater, Sale
from django.db.models import Sum, F
from datetime import datetime
from django.contrib import messages
from datetime import date, timedelta

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
    if request.method == 'GET':
        dateInputStr = request.GET.get('date')
        try:
            dateInput = datetime.strptime(dateInputStr, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            messages.error(request, 'Invalid date format')
            return redirect("home")
        
        today = date.today()
        pastDate = today - timedelta(days=365)
        futuredate = today + timedelta(days=365)
        if  dateInput > futuredate or dateInput < pastDate :
            messages.error(request, 'Date must be within 1 year of today')
            return redirect("home")
        
        sales_by_date = Sale.objects.filter(date=dateInputStr)
        sales_by_theater = (
            sales_by_date
                .values('theater')
                .annotate(name = F('theater__name'), total_sum=Sum('amount'), total_tickets=Sum('tickets_sold'), cost_per_ticket=Sum('amount') / Sum('tickets_sold'))
        )
        top_theater_name = topTheaterByRevenue(sales_by_theater)
        top_theater_by_tickets_name = topTheaterByTicketsSold(sales_by_theater)

        sales_by_movies = (
            sales_by_date
                .values('movie')
                .annotate(name = F('movie__name'), genre=F('movie__genre'), total_sum=Sum('amount'))
        )
        best_selling_movie = sales_by_movies.order_by("-total_sum").first()

        return render(request, "boxoffice/revenue_summary.html", 
                      {"date": dateInput, 
                       "sales_by_theater" : sales_by_theater, 
                       "top_theater": top_theater_name, 
                       "top_theater_by_tickets": top_theater_by_tickets_name, 
                       "best_selling_movie": best_selling_movie})

def topTheaterByTicketsSold(sales_by_theater):
    top_theater_by_tickets = sales_by_theater.order_by("-total_tickets").first()
    top_theater_by_tickets_name = top_theater_by_tickets['name'] if top_theater_by_tickets else ""
    return top_theater_by_tickets_name

def topTheaterByRevenue(sales_by_theater):
    top_theater = sales_by_theater.order_by("-total_sum").first()
    top_theater_name = top_theater['name'] if top_theater else  ""
    return top_theater_name

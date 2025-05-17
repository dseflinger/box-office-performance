from django.shortcuts import render
from boxoffice.models import Movie, Theater, Sale
from django.db.models import Sum, Max, F

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
    #todo validate date field
    if request.method == 'GET':
        date = request.GET.get('date')
        sales_by_theater = salesByTheater(date)
        top_theater_name = topTheaterByRevenue(sales_by_theater)
        top_theater_by_tickets_name = topTheaterByTicketsSold(sales_by_theater)

        #avg cost per ticket?
        #best selling genre
        #best selling movie
        #also have a return to home button
        #maybe return an aggregation by theater - theater name, total amount sold that day, total tickets sold that day, price per ticket? 
        return render(request, "boxoffice/revenue_summary.html", 
                      {"date": date, "sales_by_theater" : sales_by_theater, "top_theater": top_theater_name, "top_theater_by_tickets": top_theater_by_tickets_name})

def salesByTheater(date):
    sales_by_theater = (
            Sale.objects
                .filter(date=date)
                .values('theater')
                .annotate(name = F('theater__name'), total_sum=Sum('amount'), total_tickets=Sum('tickets_sold'))
        )
    
    return sales_by_theater

def topTheaterByTicketsSold(sales_by_theater):
    top_theater_by_tickets = sales_by_theater.order_by("-total_tickets").first()
    top_theater_by_tickets_name = top_theater_by_tickets['name'] if top_theater_by_tickets else None
    return top_theater_by_tickets_name

def topTheaterByRevenue(sales_by_theater):
    top_theater = sales_by_theater.order_by("-total_sum").first()
    top_theater_name = top_theater['name'] if top_theater else None
    return top_theater_name

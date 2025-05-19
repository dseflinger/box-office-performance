from django.contrib import admin
from django.urls import path, include
from boxoffice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('movies', views.movies_list, name='movies'),
    path('theaters', views.theaters_list, name='theaters'),
    path('sales', views.sales_list, name='sales'),
    path('revenue_summary', views.revenue_summary, name='revenue_summary'),
]

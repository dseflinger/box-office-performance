from django.contrib import admin

from boxoffice.models import Movie, Sale, Theater

# Register your models here.
admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Sale)
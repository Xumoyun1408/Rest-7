from django.contrib import admin
from .models import Header, Navbar, Category, TravelPackage

admin.site.register([Header, Navbar, Category, TravelPackage])

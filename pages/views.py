from django.shortcuts import render

from listings.models import *


# Create your views here.
def index(request):
    listings = Listing.objects.all()
    return render(
        request,
        "pages/index.html",
        {"listings": listings.order_by("list_date")[:3]},
    )


def search(request):
    return render(request, "pages/search.html")


def about(request):
    return render(request, "pages/about.html")

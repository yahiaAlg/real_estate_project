from django.shortcuts import render

from .models import *


# Create your views here.
def listings(request):

    return render(
        request,
        "listings/listings.html",
    )


def listing(request, id):
    return render(request, "listings/listing.html")

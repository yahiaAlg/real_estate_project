from django.shortcuts import render

from .models import *


# Create your views here.
def listings(request):

    return render(
        request,
        "listings/listings.html",
    )


def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "listings/listing.html", {
        "listing": listing,

    })

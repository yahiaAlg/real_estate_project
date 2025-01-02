from pprint import pprint
from django.shortcuts import render
from django.contrib import messages
from listings.models import *
from django.db.models import Q



# Create your views here.
def index(request):
    listings = Listing.objects.all()
    return render(
        request,
        "pages/index.html",
        {"listings": listings.order_by("list_date")[:3]},
    )


def search(request):
    if request.method == "POST":
        listings = Listing.objects.all()
        searched_listings = listings
        pprint(
            request.POST
        )
        keywords = request.POST.get("keywords", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        bedrooms = request.POST.get("bedrooms", "")
        price = request.POST.get("price", "")
        pprint(searched_listings)
        
        
        if keywords:
            # realtor = Realtor.objects.get(name__icontains=keywords)
            # if realtor:
            #     searched_listings.filter(realtor=realtor.id)
            #     pprint(searched_listings)
            
            # pprint(realtor)
            searched_listings = listings.filter(
                Q(title__icontains=keywords) |
                Q(description__icontains=keywords) |
                Q(address__icontains=keywords) |
                Q(realtor__name__icontains=keywords)
            )
        else:
            messages.info(request, "no keyword added")
        if city:
            searched_listings = searched_listings.filter(city=city.lower())
        else:
            messages.info(request, "no city added")

        if state:
            searched_listings = searched_listings.filter(state=state.lower())
            
        else:
            messages.info(request, "no state added")
            

        if bedrooms:
            bedrooms = int(bedrooms)
            searched_listings = searched_listings.filter(bedrooms=bedrooms)
            
        else:
            messages.info(request, "no bedroom field given")
            

        if price:
            price = float(price)
            searched_listings = searched_listings.filter(price__lte=price)
            
        else:
            messages.info(request, "no bedroom field given")
        
        pprint(searched_listings)
        
        return render(request, "pages/search.html" , {
            "searched_listings": searched_listings,
        })







def about(request):
    return render(request, "pages/about.html")

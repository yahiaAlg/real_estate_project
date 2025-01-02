from pprint import pprint
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def listings(request):

    return render(
        request,
        "listings/listings.html",
    )

def contact(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        pprint(
            request.POST
        )
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        message = request.POST.get("message","")
        
        listings = Listing.objects.get(pk=listing_id)
        if name and email and phone and message:
            contact = Contact(
                listing=listing,
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            contact.save()
            
            send_mail(
                f"contact about {listing.title}",
                f"Name: {name}\nEmail: {email}\nPhone: {phone} \n{message}",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                auth_password=settings.EMAIL_HOST_PASSWORD,
                fail_silently=False
                
            )
            print(
               "Your message has been sent!".center(100, "-")
            )
            messages.success(request, "Your message has been sent!")
        else:
            messages.success(request, "Please fill out all fields!")
        messages.success(request, "email sent successfully!")
        return redirect("listing", listing_id=listing_id)
    return 
        
        
        
        
        
        
        

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "listings/listing.html", {
        "listing": listing,

    })

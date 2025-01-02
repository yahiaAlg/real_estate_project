import datetime
from pprint import pprint
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.conf import settings

from django.core.mail import send_mail
# Create your views here.
def listings(request):
    listings = Listing.objects.all()
    return render(
        request,
        "listings/listings.html",
        {
            "listings": listings,
        }
    )

# def contact(request, listing_id):
#     listing = Listing.objects.get(pk=listing_id)
#     if request.method == "POST":
#         pprint(
#             request.POST
#         )
#         name = request.POST.get("name","")
#         email = request.POST.get("email","")
#         phone = request.POST.get("phone","")
#         message = request.POST.get("message","")
        
#         listings = Listing.objects.get(pk=listing_id)
#         if name and email and phone and message:
#             contact = Contact(
#                 listing=listing,
#                 name=name,
#                 email=email,
#                 phone=phone,
#                 message=message
#             )
#             contact.save()
            
#             send_mail(
#                 f"contact about {listing.title}",
#                 f"Name: {name}\nEmail: {email}\nPhone: {phone} \n{message}",
#                 from_email=email,
#                 recipient_list=[settings.EMAIL_HOST_USER],
#                 auth_password=settings.EMAIL_HOST_PASSWORD,
#                 fail_silently=False
                
#             )
#             print(
#                "Your message has been sent!".center(100, "-")
#             )
#             messages.success(request, "Your message has been sent!")
#         else:
#             messages.success(request, "Please fill out all fields!")
#         messages.success(request, "email sent successfully!")
#         return redirect("listing", listing_id=listing_id)
#     return 
        


def contact(request, listing_id):
    if request.method == "POST":
        contact_listing = Listing.objects.get(id=listing_id)
        name = request.POST.get("name","")
        message = request.POST.get("message","")
        phone = request.POST.get("phone","")
        email = request.POST.get("email","")
        
        if name and message and phone and email and contact_listing:
            
            
            contact = Contact(
                name=name,
                message=message,
                phone=phone,
                email=email,
                listing=contact_listing,
            )
            
            if send_mail(
                subject=f" contact about {contact_listing.title}",
                message=f"Name: {name}\nPhone: {phone} \n{message}",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                auth_password=settings.EMAIL_HOST_PASSWORD,
                fail_silently=False
            ):
                
                messages.success(
                    request,
                    "email sent successfully!"
                )
                contact.save()
                if contact:
                    messages.success(request, "contact saved into db!")
                    
                else:
                    messages.error(request, "contact not saved into db!")
            else:
                messages.error(
                    request,
                    "email not sent!"
                )
                  
    return redirect("listing", listing_id)
        
        

        
        
        
        

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "listings/listing.html", {
        "listing": listing,

    })

from django.urls import path
from . import views

urlpatterns = [
    path("listings/", views.listings, name="listings"),
    path("listing/<int:listing_id>/", views.listing, name="listing"),
    path("contact/<int:listing_id>/", views.contact, name="contact"),
    
]

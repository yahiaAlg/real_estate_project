from django.urls import path
from . import views

urlpatterns = [
    path("listings/", views.listings, name="listings"),
    path("listing/", views.listing, name="listing"),
]

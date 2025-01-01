import datetime
from django.core.management.base import BaseCommand
from listings.models import Listing, Realtor

import json


class Command(BaseCommand):
    help = "Populate database with sample realtors and listings"

    def handle(self, *args, **kwargs):
        def populate_database():
            # Create Realtors
            realtors_data = [
                {
                    "name": "John Smith",
                    "photo": "photos/realtors/agent1.jpg",
                    "description": "Top performing agent with 10 years of experience",
                    "email": "john.smith@realestate.com",
                    "phone": "555-111-2222",
                    "is_mvp": True,
                    "hire_date": datetime.datetime.strptime("2020-01-15", "%Y-%m-%d"),
                },
                {
                    "name": "Sarah Johnson",
                    "photo": "photos/realtors/agent2.jpg",
                    "description": "Specializing in luxury properties",
                    "email": "sarah.j@realestate.com",
                    "phone": "555-333-4444",
                    "is_mvp": False,
                    "hire_date": datetime.datetime.strptime("2021-03-20", "%Y-%m-%d"),
                },
                # Add more realtors as needed
            ]

            realtors_data.extend(
                [
                    {
                        "name": "Emily Davis",
                        "photo": "photos/realtors/agent3.jpg",
                        "description": "Expert in first-time homebuyers and affordable housing",
                        "email": "emily.davis@realestate.com",
                        "phone": "555-555-6666",
                        "is_mvp": True,
                        "hire_date": datetime.datetime.strptime(
                            "2018-06-25", "%Y-%m-%d"
                        ),
                    },
                    {
                        "name": "Michael Brown",
                        "photo": "photos/realtors/agent4.jpg",
                        "description": "Specializing in commercial real estate and investment properties",
                        "email": "michael.brown@realestate.com",
                        "phone": "555-777-8888",
                        "is_mvp": False,
                        "hire_date": datetime.datetime.strptime(
                            "2022-02-10", "%Y-%m-%d"
                        ),
                    },
                    {
                        "name": "Olivia Green",
                        "photo": "photos/realtors/agent5.jpg",
                        "description": "Focused on family homes and neighborhood communities",
                        "email": "olivia.green@realestate.com",
                        "phone": "555-999-0000",
                        "is_mvp": False,
                        "hire_date": datetime.datetime.strptime(
                            "2019-11-05", "%Y-%m-%d"
                        ),
                    },
                    {
                        "name": "David Wilson",
                        "photo": "photos/realtors/agent6.jpg",
                        "description": "Leading agent for waterfront and luxury properties",
                        "email": "david.wilson@realestate.com",
                        "phone": "555-123-4567",
                        "is_mvp": True,
                        "hire_date": datetime.datetime.strptime(
                            "2017-08-22", "%Y-%m-%d"
                        ),
                    },
                    {
                        "name": "Sophia Martinez",
                        "photo": "photos/realtors/agent7.jpg",
                        "description": "Expert in relocation and corporate real estate services",
                        "email": "sophia.martinez@realestate.com",
                        "phone": "555-555-7777",
                        "is_mvp": False,
                        "hire_date": datetime.datetime.strptime(
                            "2020-04-30", "%Y-%m-%d"
                        ),
                    },
                ]
            )

            # Create realtors
            created_realtors = []
            for realtor_data in realtors_data:
                realtor = Realtor.objects.create(**realtor_data)
                created_realtors.append(realtor)
                print(f"Created realtor: {realtor.name}")

            # Create Listings
            listings_data = [
                {
                    "realtor": created_realtors[0],  # John Smith
                    "title": "Beautiful Family Home",
                    "address": "123 Main Street",
                    "city": "Beverly Hills",
                    "state": "CA",
                    "zipcode": "90210",
                    "description": "Stunning 4-bedroom home with modern amenities",
                    "price": 750000,
                    "bedrooms": 4,
                    "bathrooms": 3,
                    "garage": 2,
                    "sqft": 2500,
                    "lot_size": 0.5,
                    "list_date": datetime.datetime.strptime("2024-01-01", "%Y-%m-%d"),
                    "photo_main": "photos/homes/home1_main.jpg",
                    "photo_1": "photos/homes/home1_1.jpg",
                    "photo_2": "photos/homes/home1_2.jpg",
                    "photo_3": "photos/homes/home1_3.jpg",
                    "photo_4": "photos/homes/home1_4.jpg",
                    "photo_5": "photos/homes/home1_5.jpg",
                    "photo_6": "photos/homes/home1_6.jpg",
                },
                {
                    "realtor": created_realtors[1],  # Sarah Johnson
                    "title": "Modern Downtown Condo",
                    "address": "456 Park Avenue",
                    "city": "Los Angeles",
                    "state": "CA",
                    "zipcode": "90001",
                    "description": "Luxurious 2-bedroom condo in prime location",
                    "price": 500000,
                    "bedrooms": 2,
                    "bathrooms": 2,
                    "garage": 1,
                    "sqft": 1200,
                    "lot_size": 0.0,
                    "list_date": datetime.datetime.strptime("2024-01-15", "%Y-%m-%d"),
                    "photo_main": "photos/homes/home2_main.jpg",
                    "photo_1": "photos/homes/home2_1.jpg",
                    "photo_2": "photos/homes/home2_2.jpg",
                    "photo_3": "photos/homes/home2_3.jpg",
                    "photo_4": "photos/homes/home2_4.jpg",
                    "photo_5": "photos/homes/home2_5.jpg",
                    "photo_6": "photos/homes/home2_6.jpg",
                },
                # Add more listings as needed
            ]

            listings_data.extend(
                [
                    {
                        "realtor": created_realtors[2],  # Emily Davis
                        "title": "Cozy Suburban Cottage",
                        "address": "789 Elm Street",
                        "city": "San Diego",
                        "state": "CA",
                        "zipcode": "92101",
                        "description": "Charming 3-bedroom cottage with a large backyard",
                        "price": 400000,
                        "bedrooms": 3,
                        "bathrooms": 2,
                        "garage": 1,
                        "sqft": 1500,
                        "lot_size": 0.3,
                        "list_date": datetime.datetime.strptime(
                            "2024-02-01", "%Y-%m-%d"
                        ),
                        "photo_main": "photos/homes/home3_main.jpg",
                        "photo_1": "photos/homes/home3_1.jpg",
                        "photo_2": "photos/homes/home3_2.jpg",
                        "photo_3": "photos/homes/home3_3.jpg",
                        "photo_4": "photos/homes/home3_4.jpg",
                        "photo_5": "photos/homes/home3_5.jpg",
                        "photo_6": "photos/homes/home3_6.jpg",
                    },
                    {
                        "realtor": created_realtors[3],  # Michael Brown
                        "title": "Commercial Office Space",
                        "address": "1010 Market Street",
                        "city": "San Francisco",
                        "state": "CA",
                        "zipcode": "94103",
                        "description": "Spacious office building ideal for startups",
                        "price": 1200000,
                        "bedrooms": 0,
                        "bathrooms": 4,
                        "garage": 5,
                        "sqft": 5000,
                        "lot_size": 1.0,
                        "list_date": datetime.datetime.strptime(
                            "2024-02-15", "%Y-%m-%d"
                        ),
                        "photo_main": "photos/homes/home4_main.jpg",
                        "photo_1": "photos/homes/home4_1.jpg",
                        "photo_2": "photos/homes/home4_2.jpg",
                        "photo_3": "photos/homes/home4_3.jpg",
                        "photo_4": "photos/homes/home4_4.jpg",
                        "photo_5": "photos/homes/home4_5.jpg",
                        "photo_6": "photos/homes/home4_6.jpg",
                    },
                    {
                        "realtor": created_realtors[4],  # Olivia Green
                        "title": "Spacious Family Home",
                        "address": "222 Oak Drive",
                        "city": "Sacramento",
                        "state": "CA",
                        "zipcode": "95814",
                        "description": "Beautiful 5-bedroom home with a pool",
                        "price": 850000,
                        "bedrooms": 5,
                        "bathrooms": 4,
                        "garage": 2,
                        "sqft": 3200,
                        "lot_size": 0.8,
                        "list_date": datetime.datetime.strptime(
                            "2024-03-01", "%Y-%m-%d"
                        ),
                        "photo_main": "photos/homes/home5_main.jpg",
                        "photo_1": "photos/homes/home5_1.jpg",
                        "photo_2": "photos/homes/home5_2.jpg",
                        "photo_3": "photos/homes/home5_3.jpg",
                        "photo_4": "photos/homes/home5_4.jpg",
                        "photo_5": "photos/homes/home5_5.jpg",
                        "photo_6": "photos/homes/home5_6.jpg",
                    },
                    {
                        "realtor": created_realtors[5],  # David Wilson
                        "title": "Luxury Beachfront Villa",
                        "address": "333 Ocean Avenue",
                        "city": "Malibu",
                        "state": "CA",
                        "zipcode": "90265",
                        "description": "Exclusive villa with stunning ocean views",
                        "price": 3000000,
                        "bedrooms": 6,
                        "bathrooms": 5,
                        "garage": 3,
                        "sqft": 4500,
                        "lot_size": 1.5,
                        "list_date": datetime.datetime.strptime(
                            "2024-03-15", "%Y-%m-%d"
                        ),
                        "photo_main": "photos/homes/home6_main.jpg",
                        "photo_1": "photos/homes/home6_1.jpg",
                        "photo_2": "photos/homes/home6_2.jpg",
                        "photo_3": "photos/homes/home6_3.jpg",
                        "photo_4": "photos/homes/home6_4.jpg",
                        "photo_5": "photos/homes/home6_5.jpg",
                        "photo_6": "photos/homes/home6_6.jpg",
                    },
                    {
                        "realtor": created_realtors[6],  # Sophia Martinez
                        "title": "Modern Apartment in Downtown",
                        "address": "555 City Center Blvd",
                        "city": "Los Angeles",
                        "state": "CA",
                        "zipcode": "90015",
                        "description": "Contemporary 1-bedroom apartment with city views",
                        "price": 350000,
                        "bedrooms": 1,
                        "bathrooms": 1,
                        "garage": 1,
                        "sqft": 800,
                        "lot_size": 0.0,
                        "list_date": datetime.datetime.strptime(
                            "2024-04-01", "%Y-%m-%d"
                        ),
                        "photo_main": "photos/homes/home7_main.jpg",
                        "photo_1": "photos/homes/home7_1.jpg",
                        "photo_2": "photos/homes/home7_2.jpg",
                        "photo_3": "photos/homes/home7_3.jpg",
                        "photo_4": "photos/homes/home7_4.jpg",
                        "photo_5": "photos/homes/home7_5.jpg",
                        "photo_6": "photos/homes/home7_6.jpg",
                    },
                ]
            )

            # Create listings
            for listing_data in listings_data:
                listing = Listing.objects.create(**listing_data)
                print(f"Created listing: {listing.title}")

        # Then just call it
        populate_database()

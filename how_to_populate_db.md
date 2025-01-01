Here's a Python script to add sample realtors and listings through Django shell:

```python
from datetime import datetime
from listings.models import Listing, Realtor
from django.utils import timezone

def populate_database():
    # Create Realtors
    realtors_data = [
        {
            'name': 'John Smith',
            'photo': 'photos/realtors/agent1.jpg',
            'description': 'Top performing agent with 10 years of experience',
            'email': 'john.smith@realestate.com',
            'phone': '555-111-2222',
            'is_mvp': True,
            'hire_date': '2020-01-15'
        },
        {
            'name': 'Sarah Johnson',
            'photo': 'photos/realtors/agent2.jpg',
            'description': 'Specializing in luxury properties',
            'email': 'sarah.j@realestate.com',
            'phone': '555-333-4444',
            'is_mvp': False,
            'hire_date': '2021-03-20'
        },
        # Add more realtors as needed
    ]

    # Create realtors
    created_realtors = []
    for realtor_data in realtors_data:
        realtor = Realtor.objects.create(**realtor_data)
        created_realtors.append(realtor)
        print(f"Created realtor: {realtor.name}")

    # Create Listings
    listings_data = [
        {
            'realtor': created_realtors[0],  # John Smith
            'title': 'Beautiful Family Home',
            'address': '123 Main Street',
            'city': 'Beverly Hills',
            'state': 'CA',
            'zipcode': '90210',
            'description': 'Stunning 4-bedroom home with modern amenities',
            'price': 750000,
            'bedrooms': 4,
            'bathrooms': 3,
            'garage': 2,
            'sqft': 2500,
            'lot_size': 0.5,
            'list_date': '2024-01-01',
            'photo_main': 'photos/homes/home1_main.jpg',
            'photo_1': 'photos/homes/home1_1.jpg',
            'photo_2': 'photos/homes/home1_2.jpg',
            'photo_3': 'photos/homes/home1_3.jpg',
            'photo_4': 'photos/homes/home1_4.jpg',
            'photo_5': 'photos/homes/home1_5.jpg',
            'photo_6': 'photos/homes/home1_6.jpg',
        },
        {
            'realtor': created_realtors[1],  # Sarah Johnson
            'title': 'Modern Downtown Condo',
            'address': '456 Park Avenue',
            'city': 'Los Angeles',
            'state': 'CA',
            'zipcode': '90001',
            'description': 'Luxurious 2-bedroom condo in prime location',
            'price': 500000,
            'bedrooms': 2,
            'bathrooms': 2,
            'garage': 1,
            'sqft': 1200,
            'lot_size': 0.0,
            'list_date': '2024-01-15',
            'photo_main': 'photos/homes/home2_main.jpg',
            'photo_1': 'photos/homes/home2_1.jpg',
            'photo_2': 'photos/homes/home2_2.jpg',
            'photo_3': 'photos/homes/home2_3.jpg',
            'photo_4': 'photos/homes/home2_4.jpg',
            'photo_5': 'photos/homes/home2_5.jpg',
            'photo_6': 'photos/homes/home2_6.jpg',
        },
        # Add more listings as needed
    ]

    # Create listings
    for listing_data in listings_data:
        listing = Listing.objects.create(**listing_data)
        print(f"Created listing: {listing.title}")

if __name__ == "__main__":
    try:
        populate_database()
        print("Database populated successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

To use this script:

1. Save it as `populate_db.py` in your Django project directory

2. Open Django shell:
```bash
python manage.py shell
```

3. In the shell, run:
```python
exec(open('populate_db.py').read())
```

Or alternatively, you can create a custom management command:

1. Create a new file `listings/management/commands/populate_db.py`:

```python
from django.core.management.base import BaseCommand
from listings.models import Listing, Realtor

class Command(BaseCommand):
    help = 'Populate database with sample realtors and listings'

    def handle(self, *args, **kwargs):
        # Copy the populate_database() function here
        # Then just call it
        populate_database()
```

2. Then run:
```bash
python manage.py populate_db
```

The script creates sample realtors and listings with realistic data. You can modify the `realtors_data` and `listings_data` lists to add more entries or change the existing ones. Make sure to:

1. Adjust the photo paths according to your media setup
2. Update the dates as needed
3. Add more variety in the sample data
4. Modify the prices, sizes, and other numerical values to match your needs


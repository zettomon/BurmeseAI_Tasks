###

# Generated by DeepSeek
# The only purpose is to seed random mock data into the app

###

import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from submission_portal.models import DataEntry 

class Command(BaseCommand):
    help = 'Seeds the database with 100 mock DataEntry records.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Generate 100 mock DataEntry records
        for i in range(100):
            category = random.choice(['food', 'salary', 'car_oil', 'groom'])

            # Generate mock content based on the category
            if category == 'text':
                content = f"This is a sample text content for entry {i + 1}."
            else:
                content = f"https://example.com/image_{i + 1}.jpg"
            

            # Randomly set 'is_reviewed' to True or False
            is_reviewed = random.choice([True, False])

            # Create and save the DataEntry instance
            DataEntry.objects.create(
                content=content,
                category=category,
                is_reviewed=is_reviewed
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded 100 DataEntry records!"))
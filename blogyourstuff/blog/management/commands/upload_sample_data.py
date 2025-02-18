import json
import os
from django.core.management.base import BaseCommand
from accounts.models import UserProfile
from blog.models import BlogPost

class Command(BaseCommand):
    help = 'Uploads blog post sample data into the database'

    def handle(self, *args, **options):
        # Get the path to the fixtures directory
        fixtures_dir = os.path.join('blog', 'fixtures')
        file_path = os.path.join(fixtures_dir, 'sample_data.json')

        # Load sample data from JSON file
        with open(file_path, 'r') as file:
            sample_data = json.load(file)

        # Create blog posts
        for data in sample_data:
            author = UserProfile.objects.get(first_name='root')
            BlogPost.objects.create(author=author, **data)

        self.stdout.write(self.style.SUCCESS('Blog post sample data uploaded successfully'))

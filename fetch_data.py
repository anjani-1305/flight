
from django.core.management.base import BaseCommand
from data.models import APIData
import requests

class Command(BaseCommand):
    help = 'Fetch data from API and store it in the database'

    def handle(self, *args, **kwargs):
        api_url = 'https://api.weather.gov/'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            
            for item in data:
                api_data = APIData(
                    name=item['name'],
                    description=item['description'],
                    created_at=item['created_at'],
                    updated_at=item['updated_at'],
                )
                api_data.save()
                
            self.stdout.write(self.style.SUCCESS('Data stored successfully'))
        else:
            self.stderr.write(self.style.ERROR('Failed to fetch data from API'))

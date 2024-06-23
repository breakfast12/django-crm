from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Seed initial data into the User table'

    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', email='admin@mailinator.com', password=make_password('123xixihaha'))
        self.stdout.write(self.style.SUCCESS('Successfully seeded User table'))

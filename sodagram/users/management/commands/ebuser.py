from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):

        User = get_user_model()
        User.objects.create_superuser('admin', 'admin@example.com', 'password')
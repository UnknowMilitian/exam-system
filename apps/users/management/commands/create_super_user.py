from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a new user"

    def handle(self, *args, **kwargs):
        user, _ = get_user_model().objects.get_or_create(
            email="admin@example.com", is_staff=True, is_superuser=True, is_active=True
        )

        user.set_password("admin")
        user.save()

        self.stdout.write(self.style.SUCCESS(f"Superuser object created"))

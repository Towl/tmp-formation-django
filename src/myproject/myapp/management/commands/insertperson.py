from django.core.management.base import BaseCommand, CommandError
from myproject.myapp import models


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            models.Person.objects.create(login="auto-test")
        except Exception as e:
            raise CommandError(e)

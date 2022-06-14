import logging
from django.core.management.base import BaseCommand, CommandError
from myproject.myapp import models

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, *args, **kwargs):
        try:
            models.Person.objects.get_or_create(username=kwargs['name'],login=kwargs['name'])
        except Exception as e:
            raise CommandError(e)

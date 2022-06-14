import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from myproject.myapp import models

logger = logging.getLogger(__name__)

@receiver(post_save, sender=models.Person)
def log_new_user(sender, **kwargs):
    if kwargs['created']:
        logger.info(f"New user: {kwargs['instance']}")

from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.core.management import call_command


@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    if sender.name == 'django.contrib.contenttypes':
      call_command('create_super_user')
      call_command('generate_tests')
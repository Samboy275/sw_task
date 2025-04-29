from django.dispatch import receiver
from django.db.models.signals import post_migrate, pre_save
from .models import Category


@receiver(post_migrate, sender=Category)
def add_default_data(sender, instance, **kwargs):
    """ Add default data to the database during migration """
    Category.objects.get_or_create(name="A", level=0)
    Category.objects.get_or_create(name="B", level=0)


@receiver(pre_save, sender=Category)
def  set_level(sender, instance, **kwargs):
    """ Setting the current hierarchy level for the current category """
    instance.level = instance.parent.level + 1 if instance.parent else 0

from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categories'


    def ready(self):

        # Importing signals to listen to events
        import categories.signals

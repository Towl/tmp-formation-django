from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myproject.myapp"

    def ready(self):
        from myproject.myapp import signals

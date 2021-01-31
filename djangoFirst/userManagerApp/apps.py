from django.apps import AppConfig


class UsermanagerappConfig(AppConfig):
    name = 'userManagerApp'

    def ready(self):
        import userManagerApp.signals
from django.apps import AppConfig

class MatcherAppConfig(AppConfig):
    name = 'matcher_app'

    def ready(self):
        import matcher_app.signals

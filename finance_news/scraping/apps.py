from django.apps import AppConfig


__all__ = ['ScrapingApp']


class ScrapingApp(AppConfig):
    name = 'finance_news.scraping'
    label = 'fn_scraping'

    def ready(self):
        from finance_news.scraping.tasks import __all__  # noqa

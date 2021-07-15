import logging

from finance_news.celery import app
from finance_news.scraping.service.news_collector_service import NewsCollectorService
from finance_news.scraping.tasks import BaseTask, DispatchTask

logger = logging.getLogger(__name__)


class NewsBuildCallback:
    """
    Callback class for jobs related to results. Saving parsed feed into db.
    """
    def __call__(self, results, *args, **kwargs):
        from finance_news.scraping.models import NewsItem
        NewsItem.bulk_get_or_create(results, **kwargs)


class NewsCollectorTask(BaseTask):
    """
    Task calling scraping service to parse feed
    """
    name = 'news_collector_task'
    callback = NewsBuildCallback

    def execute(self, *args, **kwargs):
        """
        Main execution function of task with whole business logic
        :param args: Optional, in this case empty list
        :param kwargs: Need to have ticker and region fields
        :return:
        """
        ticker = kwargs['ticker']
        region = kwargs['region']
        lang = kwargs.get('lang')
        news_collector_service = NewsCollectorService.build(ticker, region, lang)
        results = news_collector_service.run()
        return results


NewsCollectorTask = app.register_task(NewsCollectorTask())


class NewsCollectorDispatchTask(DispatchTask):
    """
    Task for bulk process. Send tickers as list inside kwargs param. E.g
    kwargs = {'tickers': ['AAPL', 'TWRT', 'MSFT'], 'region': 'US', 'lang': 'en-US'}
    """
    name = 'news_collector_dispatch_task'
    task = NewsCollectorTask

    def generate_collector_tasks(self, tickers, region, lang=None):
        for ticker in tickers:
            yield {'ticker': ticker, 'region': region, 'lang': lang}


NewsCollectorDispatchTask = app.register_task(NewsCollectorDispatchTask())

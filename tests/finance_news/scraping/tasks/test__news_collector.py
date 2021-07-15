import os
from unittest.mock import patch

import feedparser
from django.test import TestCase, override_settings

from finance_news.scraping.models import NewsItem
from finance_news.scraping.tasks import NewsCollectorDispatchTask, NewsCollectorTask
from settings.common import BASE_DIR


class TestNewsCollectorTask(TestCase):
    def setUp(self) -> None:
        self.tickers = ['AAPL', 'YHOO', 'MSFT']
        self.region = 'US'
        self.lang = 'en-US'

    def test__generate_collector_tasks(self):
        tickers = NewsCollectorDispatchTask.generate_collector_tasks(tickers=self.tickers, region=self.region, lang=self.lang)
        expected_tickers = [
            {
                'ticker': self.tickers[0],
                'region': self.region,
                'lang': self.lang
            }, {
                'ticker': self.tickers[1],
                'region': self.region,
                'lang': self.lang
            }, {
                'ticker': self.tickers[2],
                'region': self.region,
                'lang': self.lang
            }
        ]
        self.assertEqual(list(tickers), expected_tickers)

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @patch.object(NewsCollectorTask, 'execute')
    def test__news_collector_task(self, mock_execute_task):
        initial_news = NewsItem.objects.exists()
        self.assertFalse(initial_news)

        parsed_feed = feedparser.parse(os.path.join(BASE_DIR, 'tests', 'fixture', 'success_data.xml')).entries
        mock_execute_task.return_value = parsed_feed
        kwargs = {'ticker': 'AAPL', 'region': 'US', 'lang': 'en-US'}
        NewsCollectorTask.delay(**kwargs)
        news = NewsItem.objects.exists()
        self.assertTrue(news)
        news_item: NewsItem = NewsItem.objects.first()
        self.assertEqual(news_item.entity.ticker, kwargs['ticker'])
        self.assertEqual(str(news_item.guid), parsed_feed[0].id)
        self.assertEqual(news_item.title, parsed_feed[0].title)

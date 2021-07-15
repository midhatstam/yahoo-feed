from unittest.mock import patch

from tests.fixture.data import success_data, error_data
from django.test import TestCase
from feedparser import FeedParserDict

from finance_news.scraping.service.news_collector_service import NewsCollectorService
from utils.exception import FeedNotAvailableError


class TestNewsCollectorService(TestCase):
    def setUp(self) -> None:
        self.ticker = 'AAPL'
        self.region = 'US'
        self.lang = 'en-US'
        self.news_collector_service = NewsCollectorService.build(ticker=self.ticker, region=self.region, lang=self.lang)
        self.url = f'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US'

    def test__parse_url(self):
        url = self.news_collector_service.parse_url()
        self.assertEqual(self.url, url)

    @patch.object(NewsCollectorService, 'feed_parser')
    def test__get_xml(self, feedparser_mock):
        feedparser_mock.return_value = FeedParserDict(success_data)
        entries = self.news_collector_service.run()
        self.assertEqual(entries, feedparser_mock.return_value.entries)

    @patch.object(NewsCollectorService, 'feed_parser')
    def test__get_xml_400_error(self, feedparser_mock):
        feedparser_mock.return_value = FeedParserDict(error_data)
        self.news_collector_service.run()
        self.assertRaises(FeedNotAvailableError)
        self.assertRaisesMessage(FeedNotAvailableError, 'Feed not available')

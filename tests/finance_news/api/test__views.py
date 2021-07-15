import datetime
import uuid

from rest_framework.test import APIClient

from django.urls import reverse
from django.test import TestCase

from finance_news.scraping.models import NewsItem, Entity


class TestNewsFetchAPI(TestCase):

    def setUp(self) -> None:
        self.entity = Entity.objects.create(ticker='AAPL')
        self.title = 'Test title'
        self.link = 'http://test.com'
        self.guid = uuid.uuid4()
        self.description = 'Test description'
        self.pub_date = datetime.datetime.now()
        self.region = 'US'
        self.news_item = NewsItem(entity=self.entity, title=self.title, link=self.link, guid=self.guid,
                                  description=self.description, pub_date=self.pub_date, region=self.region)
        self.news_item.save()

    def test__list(self):
        self.assertTrue(NewsItem.objects.exists())

        url = reverse('news-list')
        client = APIClient()
        resp = client.get(url)
        self.assertEqual(resp.status_code, 200)
        json_resp = resp.json()
        self.assertIsNotNone(json_resp.get('results'))
        self.assertEqual(json_resp.get('count'), 1)
        self.assertIsNone(json_resp.get('next'))
        self.assertIsNone(json_resp.get('previous'))
        result = json_resp.get('results')[0]
        self.assertEqual(result.get('ticker'), self.entity.ticker)
        self.assertEqual(result.get('title'), self.title)
        self.assertEqual(result.get('link'), self.link)
        self.assertEqual(result.get('guid'), str(self.guid))
        self.assertEqual(result.get('description'), self.description)
        self.assertEqual(datetime.datetime.strptime(result.get('pub_date'), '%Y-%m-%dT%H:%M:%S.%fZ'), self.pub_date)
        self.assertEqual(result.get('region'), self.region)

import logging
import os
from typing import Optional

import feedparser
from feedparser import FeedParserDict

from settings.common import FEED_BASE_URL, FEED_RSS_PATH, FEED_VERSION, FEED_TYPE
from utils.exception import FeedNotAvailableError

logger = logging.getLogger(__name__)


class NewsCollectorService:
    """
    Service for parsing feed
    """
    def __init__(self, ticker: str, region: str, lang: Optional[str] = None):
        """
        :param ticker: ticker symbol, e.g: AAPL, YHOO, TWTR
        :param region: country code, e.g: US, CN
        :param lang: language code with country code, e.g: en-US. Optional field
        """
        self.ticker = ticker
        self.region = region
        self.lang = lang

    @staticmethod
    def build(ticker: str, region: str, lang: Optional[str] = None):
        return NewsCollectorService(ticker, region, lang)

    def parse_url(self) -> str:
        api_url = os.path.join(FEED_BASE_URL, FEED_RSS_PATH, FEED_VERSION, FEED_TYPE)
        return f'{api_url}?s={self.ticker}&region={self.region}&lang={self.lang}'

    def feed_parser(self) -> FeedParserDict:
        return feedparser.parse(self.parse_url())

    @staticmethod
    def check_status(feed):
        if feed.status == '400':
            raise FeedNotAvailableError
        return feed

    def run(self) -> list:
        parsed_feed: FeedParserDict = self.check_status(self.feed_parser())
        return parsed_feed.entries

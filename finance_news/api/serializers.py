from rest_framework import serializers

from finance_news.scraping.models import NewsItem


class NewsSerializer(serializers.ModelSerializer):
    ticker = serializers.CharField(source='entity.ticker')

    class Meta:
        model = NewsItem
        fields = ('id', 'ticker', 'title', 'link', 'guid', 'description', 'pub_date', 'region', 'created_by',
                  'created_at', 'updated_by', 'updated_at')

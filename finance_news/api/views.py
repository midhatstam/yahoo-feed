from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from finance_news.api.serializers import NewsSerializer
from finance_news.scraping.models import NewsItem


class NewsFilter(filters.FilterSet):
    ticker = filters.CharFilter(field_name='entity__ticker')

    class Meta:
        model = NewsItem
        fields = ('ticker', 'region', 'guid')


class NewsFetchView(mixins.ListModelMixin, GenericViewSet):
    """
    API endpoint fetching news from db with pagination and filters and no authentication
    """
    serializer_class = NewsSerializer
    queryset = NewsItem.objects.select_related('entity')
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = NewsFilter

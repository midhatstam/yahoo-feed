import logging
from datetime import datetime
from time import mktime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from safedelete import SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager
from safedelete.models import SafeDeleteModel

from finance_news.scraping.models.entity import Entity
from utils.models import AuditMixin


__all__ = ['NewsItem']

logger = logging.getLogger(__name__)


class NewsItem(AuditMixin, SafeDeleteModel):

    class Meta:
        db_table = 'news'
        verbose_name = _('Financial News')
        verbose_name_plural = _('Financial News')
        unique_together = ('guid', 'entity', 'region')

    objects = SafeDeleteManager()
    _safedelete_policy = SOFT_DELETE_CASCADE

    entity = models.ForeignKey(Entity, verbose_name=_('Entity'), db_column='entity_id', on_delete=models.DO_NOTHING)
    title = models.CharField(_('Title'), db_column='title', max_length=250)
    link = models.URLField(_('Link'), db_column='link')
    guid = models.UUIDField(_('Guid'), db_column='guid')
    description = models.TextField(_('Description'), db_column='description')
    pub_date = models.DateTimeField(_('Publication date'), db_column='pub_date')
    region = models.CharField(_('Region'), db_column='region', max_length=255)

    @classmethod
    def bulk_get_or_create(cls, items, **kwargs):
        ticker = kwargs['ticker']
        region = kwargs['region']
        entity, created = Entity.objects.get_or_create(ticker=ticker)
        for item in items:
            cls.objects.get_or_create(
                entity=entity, guid=item.id, region=region,
                defaults={
                    'title': item.title,
                    'link': item.link,
                    'description': item.summary,
                    'pub_date': datetime.fromtimestamp(mktime(item.published_parsed))
                }
            )

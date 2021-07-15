from django.db import models
from django.utils.translation import ugettext_lazy as _
from safedelete.models import SafeDeleteModel

from utils.models import AuditMixin

__all__ = ['Entity']


class Entity(AuditMixin, SafeDeleteModel):
    class Meta:
        db_table = 'entity'
        verbose_name = _('Entity')
        verbose_name_plural = _('Entities')

    ticker = models.CharField(_('Ticker'), db_column='ticker', max_length=10, db_index=True)


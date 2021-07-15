from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery("yahoo-finance-tasks")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.Task.resultrepr_maxsize = 2048

app.conf.update(
    enable_utc=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    task_queue_max_priority=10,
    result_backend='django-db',
    task_ignore_result=True,
    task_store_errors_even_if_ignored=False,
    broker_connection_max_retries=0,
    broker_pool_limit=50,
    task_inherit_parent_priority=True,
    worker_hijack_root_logger=False,
    worker_send_task_events=True,
    task_send_sent_event=True,
    event_queue_ttl=None,
    event_queue_expires=None
)

app.conf.task_default_queue = 'celery'
app.autodiscover_tasks()

app.conf.task_routes = {
    'news_collector_task': {
        'queue': 'celery'
    },
}

import logging
from celery import Task, group
from django.conf import settings

logger = logging.getLogger(__name__)

__all__ = [
    'BaseTask',
    'DispatchTask',
    'NewsCollectorTask',
    'NewsCollectorDispatchTask'
]


class BaseTask(Task):
    """
    Base task implementation, executing task's job, calling callback class if provided, returning results of main task job
    """
    abstract = True
    # ----------
    name = None
    callback = None

    def execute(self, *args, **kwargs):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        local_params = locals()
        logger.info(f"'{self.name}' with params '{local_params}' is started")

        result = self.execute(*args, **kwargs)

        if self.callback:
            self.callback()(result, *args, **kwargs)

        logger.info(f"{self.name} with params '{local_params}' is finished")

        if settings.DEBUG:
            logger.info(f'Task: {self.name}, Context: {local_params}, Result: {result}')

        return result

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.exception(exc)


class DispatchTask(Task):
    """
    Multiple tasks grouping class.
    """
    abstract = True
    # ----------
    name = None
    task = None

    def generate_collector_tasks(self, **kwargs):
        """
        Main function to prepare tasks parameters.
        :param kwargs: Parameters for calling task. E.g: tickers, region, lang
        :return: yielding ticker objects
        """
        raise NotImplementedError

    def send_tasks_to_queue(self, tasks):
        group(self.task.s(**task) for task in tasks).apply_async()
        logger.info(f"{len(tasks)} tasks sent")

    def run(self, *args, **kwargs):
        local_params = locals()
        logger.info(f"'{self.name}' with params '{local_params}' is started")
        tasks = list(self.generate_collector_tasks(**kwargs))

        self.send_tasks_to_queue(tasks)

        logger.info(f"{self.name} with params '{local_params}' is finished")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.exception(exc)


from .news_collector import NewsCollectorTask  # noqa
from .news_collector import NewsCollectorDispatchTask  # noqa

from threading import local

from django.utils.deprecation import MiddlewareMixin

_locals = local()


def get_local_variable(key, default=None):
    return getattr(_locals, key, default)


def get_current_request():
    return get_local_variable('request', None)


def get_current_user():
    request = get_current_request()
    return getattr(request, 'user', None) if request else None


class LocalMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(_locals, 'request', request)

    def process_response(self, request, response):
        if hasattr(_locals, 'request'):
            del _locals.request
        return response

    def process_exception(self, request, exception):
        if hasattr(_locals, 'request'):
            del _locals.request

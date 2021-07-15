from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import Http404

from utils.exception import Error, ProjectError
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import set_rollback

from utils.http.exception import UniqueConstraintFailed


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
    elif isinstance(exc, IntegrityError):
        exc = UniqueConstraintFailed(exc)

    if isinstance(exc, ProjectError):
        status_code = 400
        data = {
            'code': exc.code,
            'type': exc.__class__.__name__,
            'reason': getattr(exc, 'description')
        }
    elif isinstance(exc, Error):
        status_code = 400
        data = {
            'code': exc.code,
            'type': exc.__class__.__name__,
            'reason': getattr(exc, 'description')
        }
    else:
        if isinstance(exc, exceptions.APIException):
            status_code = exc.status_code
            data = {
                'code': status_code,
                'type': exc.__class__.__name__,
                'reason': exc.detail
            }
        else:
            status_code = 500
            data = {
                'code': -1,
                'type': "UnexpectedException",
                'reason': "An unexpected error has occurred."
            }
            #######################################
            ############# ATTENTION   #############
            #######################################
            # this line raises exception, remove it if it is ok for you.
            return None

    set_rollback()

    return Response(data, status=status_code)

from django.core.exceptions import (ImproperlyConfigured, ObjectDoesNotExist,
                                    ValidationError)
from rest_framework import exceptions as rest_exceptions

from .exceptions import (AmbiguityException, InvalidParameter,
                         ObjectAlreadyExists, ResourceConflict)


def get_first_matching_attr(obj, *attrs, default=None):
    for attr in attrs:
        if hasattr(obj, attr):
            return getattr(obj, attr)

    return default


def get_error_message(exc):
    if hasattr(exc, 'message_dict'):
        return exc.message_dict
    error_msg = get_first_matching_attr(exc, 'message', 'messages')

    if isinstance(error_msg, list):
        error_msg = ', '.join(error_msg)

    if error_msg is None:
        error_msg = str(exc)

    return error_msg


core_exception_to_drf_exception_mapper = {
    ObjectAlreadyExists: ResourceConflict,
    AmbiguityException: InvalidParameter,
    ImproperlyConfigured: InvalidParameter,
    ObjectDoesNotExist: InvalidParameter,
    ValidationError: rest_exceptions.ValidationError,
    PermissionError: rest_exceptions.PermissionDenied,
    ValueError: InvalidParameter,
}


def convert_to_api_exception(exc):
    if isinstance(exc, rest_exceptions.APIException):
        return exc

    api_exc_class = core_exception_to_drf_exception_mapper.get(
        exc.__class__, rest_exceptions.APIException)
    api_exc = api_exc_class(get_error_message(exc))
    return api_exc


class ExceptionHandlerMixin:
    """
    Mixin that transforms Django and Python exceptions into DRF ones.
    """
    expected_exceptions = {
        ValueError: rest_exceptions.ValidationError,
        ValidationError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied
    }

    def handle_exception(self, exc):
        api_exc = convert_to_api_exception(exc)
        response = super().handle_exception(api_exc)

        # if not response:
        #     return None

        response.data = {
            'errors': response.data
        }

        return response

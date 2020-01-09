import rest_framework.exceptions as drf_exceptions
from rest_framework import status


class ObjectAlreadyExists(Exception):
    """Object already exists"""
    pass


class AmbiguityException(Exception):
    """Multiple results returned while expecting single."""
    pass


class ResourceConflict(drf_exceptions.APIException):
    """Resource conflict."""
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Resource Conflict.'
    default_code = 'resource_conflict'


class InvalidParameter(drf_exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid Parameter.'
    default_code = 'invalid_parameter'

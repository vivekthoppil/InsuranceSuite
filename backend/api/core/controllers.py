from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveAPIView)
from rest_framework.views import APIView

from .mixins import ExceptionHandlerMixin


class BaseController(ExceptionHandlerMixin, APIView):
    pass


class GenericController(ExceptionHandlerMixin, GenericAPIView):
    pass


class GenericListController(ExceptionHandlerMixin, ListAPIView):
    pass


class GenericRetrieveController(ExceptionHandlerMixin, RetrieveAPIView):
    pass

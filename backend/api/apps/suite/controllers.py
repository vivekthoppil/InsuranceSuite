from rest_framework.permissions import IsAuthenticated

from api.core.controllers import (GenericListController,
                                  GenericRetrieveController)
from api.core.pagination import BasicPagination

from .renderers import RiskTypeRenderer
from .serializers import RiskTypeDetailSerializer, RiskTypeSearchSerializer
from .services import get_all_risk_types, get_risk_type


class RiskTypeListController(GenericListController):
    """To list all valid risk types.

    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RiskTypeRenderer,)
    pagination_class = BasicPagination
    serializer_class = RiskTypeSearchSerializer

    def get_queryset(self):
        qs = get_all_risk_types(include_deleted=False)
        return qs


class RiskTypeDetailController(GenericRetrieveController):
    """To retrieve the details of a risk type.

    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RiskTypeRenderer,)
    serializer_class = RiskTypeDetailSerializer

    def get_object(self):
        obj = get_risk_type(risk_type_id=self.kwargs['risk_type_id'])
        self.check_object_permissions(self.request, obj)
        return obj

from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist

from .models import RiskType


def get_all_risk_types_and_details(include_deleted=False,
                                   prefetch_related=False):
    if include_deleted:
        queryset = RiskType.objects.all()
    else:
        queryset = RiskType.objects.get_active()

    if prefetch_related:
        queryset = queryset.prefetch_related('attributes',
                                             'attributes__attribute_type')
    return queryset


def get_all_risk_types(include_deleted=False):
    if include_deleted:
        return RiskType.objects.get_basic_info()
    return RiskType.objects.get_active().get_basic_info()


def get_risk_type(risk_type_id):
    if not risk_type_id:
        raise ImproperlyConfigured('Invalid Risk Type Identifier')
    try:
        risk_type = RiskType.objects.get(id=risk_type_id)
    except RiskType.DoesNotExist:
        raise ObjectDoesNotExist('Requested Risk Type not found')
    return risk_type

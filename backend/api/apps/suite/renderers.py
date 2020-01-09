from api.core.renderers import CoreJSONRenderer


class RiskTypeRenderer(CoreJSONRenderer):
    object_label = 'risk_type'
    pagination_object_label = 'risk_types'

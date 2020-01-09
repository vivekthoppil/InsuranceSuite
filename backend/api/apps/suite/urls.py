from django.conf.urls import url

from .controllers import RiskTypeDetailController, RiskTypeListController

app_name = 'suite'

urlpatterns = [
    url(r'^risk_types/?$', RiskTypeListController.as_view(),
        name='list-risk-types'),
    url(r'^risk_types/(?P<risk_type_id>[0-9]+)/$',
        RiskTypeDetailController.as_view(), name='risk-type-detail')
]

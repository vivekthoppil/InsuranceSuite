from datetime import datetime

from django.db import models

from api.core.models import TimestampEntry

from .managers import RiskTypeManager


class AttributeType(models.Model):
    name = models.CharField(max_length=60, unique=True, null=False,
                            blank=False)
    description = models.CharField(max_length=100)


class RiskType(TimestampEntry):
    name = models.CharField(max_length=60, unique=True, null=False,
                            blank=False)
    description = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    objects = RiskTypeManager()


class Attribute(models.Model):
    attribute_type = models.ForeignKey(AttributeType,
                                       on_delete=models.PROTECT,
                                       null=False)
    label = models.CharField(max_length=60, null=False,
                             blank=False)
    options = models.CharField(max_length=255, null=True,
                               blank=True)
    risk_type = models.ForeignKey(RiskType, on_delete=models.PROTECT,
                                  null=False, related_name='attributes',
                                  related_query_name='attribute')
    description = models.CharField(max_length=100)
    required = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('label', 'risk_type',)


class Risk(TimestampEntry):
    risk_type = models.ForeignKey(RiskType, on_delete=models.PROTECT,
                                  null=False, related_name='risks',
                                  related_query_name='risk')
    deleted = models.BooleanField(default=False)


class RiskAttribute(TimestampEntry):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE,
                             null=False)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT,
                                  null=False, related_name='+',
                                  related_query_name='risk_attribute')
    raw_value = models.CharField(max_length=60)

    @property
    def value(self):
        if not self.raw_value:
            return self.raw_value

        attr_type = self.attribute.attribute_type.name
        if attr_type.lower() == 'date':
            return datetime.strptime(self.raw_value, 'YYYY-MM-DD')

        if attr_type.lower() == 'number':
            if '.' in self.raw_value:
                return float(self.raw_value)
            return int(self.raw_value)

        return self.raw_value

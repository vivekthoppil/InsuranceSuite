from django.db import models

from .query import RiskTypeQuerySet


class RiskTypeManager(models.Manager):
    def get_queryset(self):
        return RiskTypeQuerySet(self.model, using=self.db)

    def get_active(self):
        return self.get_queryset().get_non_deleted()

    def get_basic_info(self):
        return self.get_queryset().get_basic_info()

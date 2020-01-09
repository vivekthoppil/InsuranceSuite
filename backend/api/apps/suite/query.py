from django.db import models


class RiskTypeQuerySet(models.QuerySet):
    def get_non_deleted(self):
        return self.filter(deleted=False)

    def get_basic_info(self):
        return self.values('id', 'name', 'description', 'deleted')

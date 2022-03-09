from django.conf import settings
from django.db import models


class Acc40RawDataManager(models.Manager):

    def get_queryset(self):
        return super(Acc40RawDataManager, self).get_queryset().using(settings.ACC40_DATABASE_ROUTE)

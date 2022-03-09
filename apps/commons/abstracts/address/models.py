from .choices import THAI_PROVICE
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractAddress(models.Model):
    is_default = models.BooleanField(default=False, verbose_name=_('Default'))
    address_name = models.CharField(max_length=255, verbose_name=_("Calling Address Name"))
    street = models.TextField(blank=True, verbose_name=_("Street"))
    province = models.IntegerField(
        choices=THAI_PROVICE,
        default=THAI_PROVICE.BANGKOK,
        verbose_name=_("Province")
    )
    zipcode = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(10000),
            MaxValueValidator(99999)
        ],
        verbose_name=_("Zipcode")
    )

    class Meta:
        abstract = True

import random

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractDocument(models.Model):
    reference_document = models.CharField(
        max_length=255,
        editable=False,
        unique=True,
        db_index=True,
        verbose_name=_('Document Code')
    )

    class Meta:
        abstract = True

    def render_reference_document_pattern(self):
        raise NotImplementedError(_("Unknown Reference Document Pattern"))

    def document_current_create_date(self):
        return datetime.now().strftime("%Y-%m-%d")

    def document_generate_random(self):
        value = random.random()
        return str(value).split(".")[1]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.reference_document = self.render_reference_document_pattern()
        super().save(*args, **kwargs)

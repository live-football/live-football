from django.conf import settings
from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _
from livefield import LiveField
from livefield import LiveManager


class SoftDeletionModel(models.Model):
    live = LiveField()

    # django will use the first encounter manager as a default manager (so ordering matter!!)
    objects = LiveManager()
    all_objects = LiveManager(include_soft_deleted=True)

    class Meta:
        abstract = True

    def delete(self, using=None):
        self.live = False
        self.save()
        signals.post_delete.send(sender=self.__class__, instance=self)

    def hard_delete(self, using=None):
        super(SoftDeletionModel, self).delete(using=using)

    def undelete(self):
        self.live = True
        self.save()


class ControlModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_user",
        verbose_name=_('Created User')
    )
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated_user",
        verbose_name=_('Edited User')
    )

    class Meta:
        abstract = True

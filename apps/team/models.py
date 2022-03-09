import reversion
from apps.commons.models.mixins import SoftControlModel
from django.db import models
from django.utils.translation import ugettext_lazy as _


@reversion.register()
class Team(SoftControlModel):
    

    name = models.CharField(
        null=True, 
        blank=True,
        max_length=300, 
        verbose_name=_('Name')
    )

    # club = models.CharField(
    #     null=True, 
    #     blank=True,
    #     max_length=300, 
    #     verbose_name=_('Club')
    # )

    logo = models.ImageField(upload_to ='static/images/team_logo')

    def __str__(self):

        return self.name

class Meta:
    app_label = 'team'
    verbose_name = _('Football Team')
    verbose_name_plural = _('Football Team')


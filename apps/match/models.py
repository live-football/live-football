import reversion
from apps.commons.models.mixins import SoftControlModel
from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.team.models import Team
from .choices import STREAM_TOOLS


@reversion.register()
class LiveLink(SoftControlModel):
    

    link = models.CharField(
        null=True, 
        blank=True,
        max_length=300, 
        verbose_name=_('Link')
    )

    type = models.IntegerField(
        choices=STREAM_TOOLS,
        default=STREAM_TOOLS.YT,
        verbose_name=_("Type")
    )

    logo = models.ImageField(upload_to ='static/images/live_logo')



    class Meta:
        app_label = 'match'
        verbose_name = _('Live Link')
        verbose_name_plural = _('Live Link')

    def __str__(self):
        return self.link



@reversion.register()
class Match(SoftControlModel):
    

    date = models.DateTimeField(verbose_name=_('Date'))

    title = models.CharField(
        null=True, 
        blank=True,
        max_length=300, 
        verbose_name=_('Title')
    )

    home_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        blank=True, 
        null=True,
        related_name="home_team",
        verbose_name=_("Home Team")
    )

    away_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        blank=True, 
        null=True,
        related_name="away_team",
        verbose_name=_("Away Team")
    )

    live_link = models.ManyToManyField(
        LiveLink, 
        verbose_name=_("Live Link")
    )


    class Meta:
        app_label = 'match'
        verbose_name = _('Match Board')
        verbose_name_plural = _('Match Board')

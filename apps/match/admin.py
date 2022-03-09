from django.contrib import admin

# Register your models here.
from .forms import MatchForm, LiveLinkForm
from .models import Match, LiveLink
from apps.commons.admin.mixins import ControlAdmin
from django.contrib import admin
from reversion.admin import VersionAdmin


@admin.register(Match)
class MatchAdmin(ControlAdmin, VersionAdmin):
    form = MatchForm
    list_display = (
        'date',
        'title',
        'home_team',
        'away_team',
)
    list_filter = (
        'date',
        'title',
        'home_team',
        'away_team',
    )
    search_fields = (
        'date',
        'title',
        'home_name',
        'away_team',
    )


    filter_horizontal = (
        "live_link",
    )

@admin.register(LiveLink)
class LiveLinkAdmin(ControlAdmin, VersionAdmin):
    form = LiveLinkForm
    list_display = (
        'link',
        'type',
        'logo',
)
    list_filter = (
        'logo',
        'type',
        'link',
    )
    search_fields = (
        'logo',
        'type',
        'link',
    )

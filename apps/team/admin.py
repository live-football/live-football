from django.contrib import admin

# Register your models here.
from .forms import TeamForm
from .models import Team
from apps.commons.admin.mixins import ControlAdmin
from django.contrib import admin
from reversion.admin import VersionAdmin


@admin.register(Team)
class TeamAdmin(ControlAdmin, VersionAdmin):
    form = TeamForm
    list_select = (
        "name"
    )
    list_display = (
        'name',
        'logo'
    )

    # Options
    list_display_links = (
        'name',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
    )




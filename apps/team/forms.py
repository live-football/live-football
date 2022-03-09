from .models import Team
from apps.commons.forms.mixins import SoftControlControlModelFormMixin


class TeamForm(SoftControlControlModelFormMixin):
    class Meta:
        model = Team
        fields = [
            'name',
            'logo',
            'live'
        ]



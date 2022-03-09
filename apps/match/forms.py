from .models import Match, LiveLink
from apps.commons.forms.mixins import SoftControlControlModelFormMixin


class MatchForm(SoftControlControlModelFormMixin):
    class Meta:
        model = Match
        fields = [
            'date',
            'title',
            'home_team',
            'away_team',
            'live_link',
            'live'
        ]



class LiveLinkForm(SoftControlControlModelFormMixin):
    class Meta:
        model = LiveLink
        fields = [
            'link',
            'type',
            'logo',
            'live'
        ]



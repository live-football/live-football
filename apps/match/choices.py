from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


STREAM_TOOLS = Choices(
    (0, "YT", _("Youtube")),
    (1, "SCB", _("ScoreBat")),
)

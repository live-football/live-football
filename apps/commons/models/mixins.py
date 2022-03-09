from .managers import ControlModel
from .managers import SoftDeletionModel
from apps.commons.abstracts.models import AbstractToken


class SoftControlModel(AbstractToken, ControlModel, SoftDeletionModel):
    class Meta:
        abstract = True

    # custom error message that remove 'live' key
    def unique_error_message(self, model_class, unique_check):
        unique_check_list = list(unique_check)
        unique_check = tuple(field for field in unique_check_list if field != 'live')
        return super(SoftControlModel, self).unique_error_message(model_class, unique_check)


class HardControlModel(AbstractToken, ControlModel):
    class Meta:
        abstract = True

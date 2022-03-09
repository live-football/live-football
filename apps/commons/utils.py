import os

from django.utils import timezone
from django.utils.deconstruct import deconstructible
from enum import Enum
from uuid import uuid4


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s/%s/%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        # extension = os.path.splitext(filename)[1]
        now = timezone.now()
        return self.path % (uuid4(), now.date().strftime("%Y/%m/%d"), filename)


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


def enum_choice_builder(choice: Enum):
    return choice.value[0], choice.value[1]

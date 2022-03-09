from .serializers import AutomaticFieldMixin
from .serializers import CRUDSerializer
from rest_framework import serializers


class CRUDSerializerMixin(AutomaticFieldMixin, CRUDSerializer):
    live = serializers.BooleanField(default=True, write_only=True)


class WriteRestrictedModelSerializer(serializers.ModelSerializer):
    """
        A ModelSerializer that takes an additional `writable_fields` argument that controls which fields can be written to.
    """

    def __init__(self, *args, **kwargs):
        super(WriteRestrictedModelSerializer, self).__init__(*args, **kwargs)

        # Any fields set to read_only.
        for field_name in self.fields.keys():
            self.fields[field_name].read_only = True

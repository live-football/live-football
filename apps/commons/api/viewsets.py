from rest_framework import viewsets


class CRUDViewsetMixin(viewsets.ModelViewSet):
    # serializer_class = UserSerializer
    # serializer_detail_class = UserDetailSerializer
    # queryset = User.objects.all()
    # queryset_detail = queryset.prefetch_related('groups__permissions')
    pass

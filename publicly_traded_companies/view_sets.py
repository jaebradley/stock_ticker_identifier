from rest_framework.viewsets import ReadOnlyModelViewSet

from publicly_traded_companies.models import Exchange
from publicly_traded_companies.serializers import ExchangeSerializer


class ExchangeViewSet(ReadOnlyModelViewSet):
    serializer_class = ExchangeSerializer

    def get_queryset(self):
        return Exchange.objects.all().order_by('name')
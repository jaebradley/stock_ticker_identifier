from rest_framework.serializers import ModelSerializer


from publicly_traded_companies.models import Exchange


class ExchangeSerializer(ModelSerializer):
    class Meta:
        model = Exchange()
        fields = ('id', 'name', 'nickname')
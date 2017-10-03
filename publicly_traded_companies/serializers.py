from rest_framework.serializers import ModelSerializer


from publicly_traded_companies.models import Exchange, Company


class ExchangeSerializer(ModelSerializer):
    class Meta:
        model = Exchange()
        fields = ('id', 'name', 'nickname')


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company()
        fields = ('id', 'name', 'ticker', 'ipo_year', 'sector', 'industry')
from rest_framework.serializers import ModelSerializer, URLField


from publicly_traded_companies.models import Exchange, Company, Industry, Sector


class ExchangeSerializer(ModelSerializer):
    class Meta:
        model = Exchange()
        fields = ('id', 'name', 'nickname')


class IndustrySerializer(ModelSerializer):
    class Meta:
        model = Industry()
        fields = ('id', 'name')


class SectorSerializer(ModelSerializer):
    class Meta:
        model = Sector()
        fields = ('id', 'name')


class CompanySerializer(ModelSerializer):
    exchange = ExchangeSerializer()
    sector = SectorSerializer()
    industry = IndustrySerializer()

    class Meta:
        model = Company()
        fields = (
            'id',
            'name',
            'ticker',
            'exchange',
            'sector',
            'industry',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
            'zip_code',
            'fax_number',
            'phone_number',
            'website_url',
            'employee_count',
            'business_summary'
        )
from rest_framework.serializers import ModelSerializer


from publicly_traded_companies.models import Exchange, Company, Industry


class ExchangeSerializer(ModelSerializer):
    class Meta:
        model = Exchange()
        fields = ('id', 'name', 'nickname')


class IndustrySerializer(ModelSerializer):
    class Meta:
        model = Industry()
        fields = ('id', 'name')


class CompanySerializer(ModelSerializer):
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
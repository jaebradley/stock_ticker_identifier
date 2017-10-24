from graphene import relay, AbstractType, Schema, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from publicly_traded_companies.models import Exchange as ExchangeModel, Company as CompanyModel, \
    Industry as IndustryModel, Sector as SectorModel


class ExchangeNode(DjangoObjectType):
    class Meta:
        model = ExchangeModel
        filter_fields = {
            'name': ['exact', 'icontains'],
            'nickname': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class IndustryNode(DjangoObjectType):
    class Meta:
        model = IndustryModel
        filter_fields = {
            'name': ['exact', 'icontains']
        }
        interfaces = (relay.Node, )


class SectorNode(DjangoObjectType):
    class Meta:
        model = SectorModel
        filter_fields = {
            'name': ['exact', 'icontains']
        }
        interfaces = (relay.Node, )


class CompanyNode(DjangoObjectType):
    class Meta:
        model = CompanyModel
        filter_fields = {
            'name': ['exact', 'icontains'],
            'ticker': ['exact', 'icontains'],
            'sector__id': ['exact'],
            'sector__name': ['exact', 'icontains'],
            'industry__id': ['exact'],
            'industry__name': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class Query(AbstractType, ObjectType):
    exchange = relay.Node.Field(ExchangeNode)
    all_exchanges = DjangoFilterConnectionField(ExchangeNode)

    company = relay.Node.Field(CompanyNode)
    all_companies = DjangoFilterConnectionField(CompanyNode)

    industry = relay.Node.Field(IndustryNode)
    all_industries = DjangoFilterConnectionField(IndustryNode)

    sector = relay.Node.Field(SectorNode)
    all_sectors = DjangoFilterConnectionField(SectorNode)


schema = Schema(query=Query)

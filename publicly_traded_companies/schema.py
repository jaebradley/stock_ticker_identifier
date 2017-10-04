from graphene import relay, AbstractType, Schema, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from publicly_traded_companies.models import Exchange as ExchangeModel, Company as CompanyModel


class ExchangeNode(DjangoObjectType):
    class Meta:
        model = ExchangeModel
        filter_fields = {
            'name': ['exact', 'icontains'],
            'nickname': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class CompanyNode(DjangoObjectType):
    class Meta:
        model = CompanyModel
        filter_fields = {
            'name': ['exact', 'icontains'],
            'ticker': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class Query(AbstractType, ObjectType):
    exchange = relay.Node.Field(ExchangeNode)
    all_exchanges = DjangoFilterConnectionField(ExchangeNode)

    company = relay.Node.Field(CompanyNode)
    all_companies = DjangoFilterConnectionField(CompanyNode)


schema = Schema(query=Query)

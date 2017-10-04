from graphene import relay, AbstractType, Schema, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from publicly_traded_companies.models import Exchange as ExchangeModel


class ExchangeNode(DjangoObjectType):
    class Meta:
        model = ExchangeModel
        filter_fields = ['id', 'name', 'nickname']
        interfaces = (relay.Node, )


class Query(AbstractType, ObjectType):
    exchange = relay.Node.Field(ExchangeNode)
    all_exchanges = DjangoFilterConnectionField(ExchangeNode)


schema = Schema(query=Query)

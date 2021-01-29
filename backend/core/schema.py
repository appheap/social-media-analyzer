import graphene

from graphene_django.debug import DjangoDebug

from users.schema import Query as usersQuery
from telegram.schema import Query as telegramQuery


class Query(
    usersQuery,
    telegramQuery,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, auto_camelcase=False)

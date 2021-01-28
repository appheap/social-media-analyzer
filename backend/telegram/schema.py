import graphene
from graphene_django import DjangoObjectType

from .models import TelegramAccount
from .models import TelegramChannel


class TelegramAccountType(DjangoObjectType):
    class Meta:
        model = TelegramAccount
        fields = '__all__'


class Query(graphene.ObjectType):
    all_telegram_accounts = graphene.List(TelegramAccountType)

    def resolve_all_telegram_accounts(root, info):
        # We can easily optimize query count in the resolve method
        return TelegramAccount.objects.all()

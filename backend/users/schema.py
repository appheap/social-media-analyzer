import graphene
from graphene_django import DjangoObjectType

from .models import SiteUser


# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = ("id", "name", "ingredients")

class SiteUserType(DjangoObjectType):
    class Meta:
        model = SiteUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(SiteUserType)

    def resolve_all_users(root, info):
        # We can easily optimize query count in the resolve method
        return SiteUser.objects.all()

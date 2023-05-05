import graphene
from graphene_django import DjangoObjectType
from api import models
from . import event

class AnyType(DjangoObjectType):
    class Meta:
        model = models.Any
        fields = ("id", "name", "last_name")


class BannerType(DjangoObjectType):
    class Meta:
        model = models.Banner
        fields = ("id", "title", "img")


class Query(event.Query, graphene.ObjectType):
    all_anys = graphene.List(AnyType)
    all_banners = graphene.List(BannerType)
    hello = graphene.String(default_value="Hi!")

    def resolve_all_anys(root, info):
        return models.Any.objects.all()

    def resolve_all_banners(root, info):
        return models.Banner.objects.order_by('-is_main')


class Mutation(
    graphene.ObjectType
):
    pass

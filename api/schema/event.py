import graphene
from graphene_django import DjangoObjectType
from api import models
import time


class EventType(DjangoObjectType):
    class Meta:
        model = models.Event
        fields = ("__all__")


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)

    def resolve_all_events(root, info):
        return models.Event.objects.all()


class Mutation(
    graphene.ObjectType
):
    pass

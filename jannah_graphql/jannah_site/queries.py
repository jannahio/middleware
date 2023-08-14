import graphene
from graphene_django import DjangoObjectType
from jannah_site import models as jannah_models
from jannah_site import types as jannah_types


class Query(graphene.ObjectType):
    site = graphene.Field(jannah_types.JannahSiteType)
    all_users = graphene.List(jannah_types.UserType)
    all_boots = graphene.List(jannah_types.BootType)
    all_networks = graphene.List(jannah_types.NetworkType)
    all_storages = graphene.List(jannah_types.StorageType)
    all_computes = graphene.List(jannah_types.ComputeType)
    all_uxs = graphene.List(jannah_types.UXType)
    all_feedbacks = graphene.List(jannah_types.FeedbackType)

    def resolve_site(root, info):
        return (
            jannah_models.Site.objects.first()
        )
    def resolve_all_users(root, info):
        return (
            jannah_models.User.objects.all()
        )
    def resolve_all_boots(root, info):
        return (
                jannah_models.Boot.objects.all()
            )
    def resolve_all_networks(root, info):
        return (
            jannah_models.Network.objects.all()
        )

    def resolve_all_storages(root, info):
        return (
            jannah_models.Storage.objects.all()
        )

    def resolve_all_computes(root, info):
        return (
            jannah_models.Compute.objects.all()
        )


    def resolve_all_uxs(root, info):
        return (
            jannah_models.UX.objects.all()
        )

    def resolve_all_feedbacks(root, info):
        return (
            jannah_models.Feedback.objects.all()
        )
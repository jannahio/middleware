import graphene
from collections import namedtuple
from jannah_site import models as jannah_models
from jannah_site import types as jannah_types

WorkflowsValueObject = namedtuple("Workflows", [
                                                "cursor",
                                                "hasMore",
                                                "workflows"
                                                ]
                                  )

class JannahWorkflows(graphene.ObjectType):
    cursor = graphene.Int()
    hasMore = graphene.Boolean()
    workflows = graphene.List(jannah_types.WorkflowType)
    # sites = graphene.List(jannah_types.JannahSiteType)
    # users = graphene.List(jannah_types.UserType)
    # boots = graphene.List(jannah_types.BootType)
    # networks = graphene.List(jannah_types.NetworkType)
    # storages = graphene.List(jannah_types.StorageType)
    # computes = graphene.List(jannah_types.ComputeType)
    # uxs = graphene.List(jannah_types.UXType)
    # feedbacks = graphene.List(jannah_types.FeedbackType)


class Query(graphene.ObjectType):
    site = graphene.Field(jannah_types.JannahSiteType)
    sites = graphene.List(jannah_types.JannahSiteType)
    users = graphene.List(jannah_types.UserType)
    boots = graphene.List(jannah_types.BootType)
    networks = graphene.List(jannah_types.NetworkType)
    storages = graphene.List(jannah_types.StorageType)
    computes = graphene.List(jannah_types.ComputeType)
    uxs = graphene.List(jannah_types.UXType)
    feedbacks = graphene.List(jannah_types.FeedbackType)
#    workflows = graphene.ObjectType(jannah_types.WorkflowType)
    workflows = graphene.Field(JannahWorkflows)

    def resolve_workflows(parent, info):
        return JannahWorkflows(
                                cursor = 8,
                                hasMore = True,
                                workflows = jannah_models.Workflow.objects.all()
                                # sites = jannah_models.Site.objects.all(),
                                # users = jannah_models.User.objects.all(),
                                # boots = jannah_models.Boot.objects.all(),
                                # networks = jannah_models.Network.objects.all(),
                                # storages = jannah_models.Storage.objects.all(),
                                # computes = jannah_models.Compute.objects.all(),
                                # uxs = jannah_models.UX.objects.all(),
                                # feedbacks = jannah_models.Feedback.objects.all()
                            )

    def resolve_site(root, info):
        return (
            jannah_models.Site.objects.first()
        )
    def resolve_sites(root, info):
            return (
                jannah_models.Site.objects.all()
            )
    def resolve_users(root, info):
        return (
            jannah_models.User.objects.all()
        )
    def resolve_boots(root, info):
        return (
                jannah_models.Boot.objects.all()
            )
    def resolve_networks(root, info):
        return (
            jannah_models.Network.objects.all()
        )

    def resolve_storages(root, info):
        return (
            jannah_models.Storage.objects.all()
        )

    def resolve_computes(root, info):
        return (
            jannah_models.Compute.objects.all()
        )

    def resolve_uxs(root, info):
        return (
            jannah_models.UX.objects.all()
        )

    def resolve_feedbacks(root, info):
        return (
            jannah_models.Feedback.objects.all()
        )

    # def resolve_workflows(root, info):
    #     return {
    #         'cursor': 8,
    #         'workflows': jannah_models.Workflow.objects.all()
    #     }

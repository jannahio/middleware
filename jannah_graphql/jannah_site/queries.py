import graphene
from jannah_site import models as jannah_models
from jannah_site import types as jannah_types

class JannahAPIObjectType(graphene.ObjectType):
    cursor = graphene.Int()
    hasMore = graphene.Boolean()

class JannahSites(JannahAPIObjectType):
    sites = graphene.List(jannah_types.SiteType)

class JannahUsers(JannahAPIObjectType):
    users = graphene.List(jannah_types.UserType)

class JannahBoots(JannahAPIObjectType):
    boots = graphene.List(jannah_types.BootType)

class JannahNetworks(JannahAPIObjectType):
    networks = graphene.List(jannah_types.NetworkType)

class JannahStorages(JannahAPIObjectType):
    storages = graphene.List(jannah_types.StorageType)

class JannahComputes(JannahAPIObjectType):
    computes = graphene.List(jannah_types.ComputeType)

class JannahUXs(JannahAPIObjectType):
    uxs = graphene.List(jannah_types.UXType)

class JannahFeedbacks(JannahAPIObjectType):
    feedbacks = graphene.List(jannah_types.FeedbackType)

class JannahWorkflows(JannahAPIObjectType):
    workflows = graphene.List(jannah_types.WorkflowType)

class Query(graphene.ObjectType):
    sites = graphene.Field(JannahSites)
    users = graphene.Field(JannahUsers)
    boots = graphene.Field(JannahBoots)
    networks = graphene.Field(JannahNetworks)
    storages = graphene.Field(JannahStorages)
    computes = graphene.Field(JannahComputes)
    uxs = graphene.Field(JannahUXs)
    feedbacks = graphene.Field(JannahFeedbacks)
    workflows = graphene.Field(JannahWorkflows)

    def resolve_sites(root, info):
        return JannahSites(
                cursor = 8,
                hasMore = True,
                sites = jannah_models.Site.objects.all()
            )
    def resolve_users(root, info):
        return JannahUsers(
            cursor = 8,
            hasMore = True,
            users = jannah_models.User.objects.all()
        )
    def resolve_boots(root, info):
        return JannahBoots(
                cursor = 8,
                hasMore = True,
                boots = jannah_models.Boot.objects.all()
            )
    def resolve_networks(root, info):
        return JannahNetworks(
            cursor = 8,
            hasMore = True,
            networks = jannah_models.Network.objects.all()
        )
    def resolve_storages(root, info):
        return JannahStorages(
            cursor = 8,
            hasMore = True,
            storages = jannah_models.Storage.objects.all()
        )
    def resolve_computes(root, info):
        return JannahComputes(
            cursor = 8,
            hasMore = True,
            computes = jannah_models.Compute.objects.all()
        )
    def resolve_uxs(root, info):
        return JannahUXs(
            cursor = 8,
            hasMore = True,
            uxs = jannah_models.UX.objects.all()
        )
    def resolve_feedbacks(root, info):
        return JannahFeedbacks(
            cursor = 8,
            hasMore = True,
            feedbacks = jannah_models.Feedback.objects.all()
        )
    def resolve_workflows(parent, info):
        return JannahWorkflows(
            cursor = 8,
            hasMore = True,
            workflows = jannah_models.Workflow.objects.all()
        )

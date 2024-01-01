from django.core.paginator import Paginator
import graphene
from jannah_site import models as jannah_models
from jannah_site import types as jannah_types

#for managing lists of objects
class JannahAPIObjectType(graphene.ObjectType):
    cursor = graphene.String()
    count = graphene.Int()
    hasMore = graphene.Boolean()

# for managing a specific object instance
class JannahAPIObjectDetailType(graphene.ObjectType):
    id = graphene.String(required=True)

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

# class JannahWorkflowDetail(JannahAPIObjectDetailType):
#     workflowdetail = graphene.Field(jannah_types.WorkflowType)

class Query(graphene.ObjectType):
    sites = graphene.Field(JannahSites, 
                           cursor=graphene.String(),
                           count=graphene.Int()
                           )
    users = graphene.Field(JannahUsers, 
                           cursor=graphene.String(),
                           count=graphene.Int()
                           )
    boots = graphene.Field(JannahBoots, 
                           cursor=graphene.String(),
                           count=graphene.Int()
                           )
    networks = graphene.Field(JannahNetworks, 
                              cursor=graphene.String(),
                              count=graphene.Int()
                           )
    storages = graphene.Field(JannahStorages,
                              cursor=graphene.String(),
                              count=graphene.Int()
                            )
    computes = graphene.Field(JannahComputes, 
                              cursor=graphene.String(),
                              count=graphene.Int()
                             )
    uxs = graphene.Field(JannahUXs, 
                         cursor=graphene.String(),
                         count=graphene.Int()
                        )
    feedbacks = graphene.Field(JannahFeedbacks,
                               cursor=graphene.String(),
                               count=graphene.Int()
                        )
    workflows = graphene.Field(JannahWorkflows, 
                               cursor=graphene.String(),
                               count=graphene.Int()
                        )
    workflow = graphene.Field(jannah_types.WorkflowType,
                                     id=graphene.String(required=True)
                                     )

    def resolve_sites(root, info, cursor = "0", count=0):
        return JannahSites(
                cursor = "8",
                hasMore = True,
                sites = jannah_models.Site.objects.all()
            )
    def resolve_users(root, info, cursor = "0", count=0):
        return JannahUsers(
            cursor = "8",
            hasMore = True,
            users = jannah_models.User.objects.all()
        )
    def resolve_boots(root, info, cursor = "0", count=0):
        return JannahBoots(
                cursor = "8",
                hasMore = True,
                boots = jannah_models.Boot.objects.all()
            )
    def resolve_networks(root, info, cursor = "0", count=0):
        return JannahNetworks(
            cursor = "8",
            hasMore = True,
            networks = jannah_models.Network.objects.all()
        )
    def resolve_storages(root, info, cursor = "0", count=0):
        return JannahStorages(
            cursor = "8",
            hasMore = True,
            storages = jannah_models.Storage.objects.all()
        )
    def resolve_computes(root, info, cursor = "0", count=0):
        return JannahComputes(
            cursor = "8",
            hasMore = True,
            computes = jannah_models.Compute.objects.all()
        )
    def resolve_uxs(root, info, cursor = "0", count=0):
        return JannahUXs(
            cursor = "8",
            hasMore = True,
            uxs = jannah_models.UX.objects.all()
        )
    def resolve_feedbacks(root, info, cursor = "0", count=0):
        return JannahFeedbacks(
            cursor = "8",
            hasMore = True,
            feedbacks = jannah_models.Feedback.objects.all()
        )
    def resolve_workflows(parent, info, cursor = "1", count=0):
        try:
            cursor = int(cursor)
        except:
            cursor = 1
        if cursor < 1: cursor = 1
        if count == 0: count = 3
        _workflows = jannah_models.Workflow.objects.all().order_by("id")
        _pages = Paginator(_workflows, count)
        _cursor_page = _pages.page(cursor)
        return JannahWorkflows(
            cursor = str(cursor + 1) if _cursor_page.has_next() else str(cursor),
            hasMore = _cursor_page.has_next(),
            count = len(_cursor_page.object_list),
            workflows = _cursor_page.object_list
        )
    def resolve_workflow(parent, info, id):
        id = int(id)
        _workflow = jannah_models.Workflow.objects.all().get(id=id)
        return _workflow
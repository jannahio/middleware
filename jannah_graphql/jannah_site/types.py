import graphene
from graphene_django import DjangoObjectType
from jannah_site import models as jannah_models

class SiteType(DjangoObjectType):
    class Meta:
        model = jannah_models.Site

class UserType(DjangoObjectType):
    class Meta:
        model = jannah_models.User


class BootType(DjangoObjectType):
    class Meta:
        model = jannah_models.Boot

class NetworkType(DjangoObjectType):
    class Meta:
        model = jannah_models.Network

class StorageType(DjangoObjectType):
    class Meta:
        model = jannah_models.Storage

class ComputeType(DjangoObjectType):
    class Meta:
        model = jannah_models.Compute


class UXType(DjangoObjectType):
    class Meta:
        model = jannah_models.UX

class FeedbackType(DjangoObjectType):
    class Meta:
        model = jannah_models.Feedback

class WorkflowType(DjangoObjectType):
    class Meta:
        model = jannah_models.Workflow



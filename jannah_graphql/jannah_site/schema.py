import graphene
from jannah_site import queries as jannah_queries
from jannah_site import mutations as jannah_mutations

schema = graphene.Schema(query=jannah_queries.Query, mutation=jannah_mutations.Mutation)
import graphene
import hero1.schema
class Query(hero1.schema.Query, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query)

import strawberry
from strawberry_django_plus import gql
from strawberry_django_plus.directives import SchemaDirectiveExtension

from books.schema import Query as BookQuery, Mutation as BookMutation


@strawberry.type
class Query(BookQuery):
    pass


@strawberry.type
class Mutation(BookMutation):
    pass


schema = gql.Schema(query=Query, mutation=Mutation, extensions=[SchemaDirectiveExtension])

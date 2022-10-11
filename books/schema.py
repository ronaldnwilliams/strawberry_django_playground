import strawberry
from strawberry_django_plus import gql
from strawberry_django_plus.permissions import HasPerm

from books.resolvers import BookResolver
from books.types import Book


@strawberry.type
class Query:
    book: Book = gql.django.field()
    books: list[Book] = gql.django.field()


@strawberry.type
class Mutation:
    add_book: Book = gql.django.field(
        resolver=BookResolver.add,
        directives=[HasPerm(perms=['books.add_book', 'books.view_book'])],
    )

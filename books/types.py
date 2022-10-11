import strawberry

from books import models


@strawberry.django.type(model=models.Book)
class Book:
    id: strawberry.auto
    title: strawberry.auto

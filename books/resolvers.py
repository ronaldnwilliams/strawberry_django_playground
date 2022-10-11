from books.models import Book


class BookResolver:
    def add(self, title: str):
        return Book.objects.create(title=title)

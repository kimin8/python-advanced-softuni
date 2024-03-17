from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, name: str, books: List[Book]):
        self.name = name
        self.books = books

    def add_book(self, book: Book) -> str:
        self.books.append(book)
        return f"{book.title} by {book.author} added to {self.name}."

    def find_book_by_title(self, title: str) -> Book or str:
        try:
            book = next(filter(lambda b: b.title == title, self.books))
            return book
        except StopIteration:
            return "Book not found."

    def find_book_by_author(self, author: str) -> Book or str:
        try:
            book = next(filter(lambda b: b.author == author, self.books))
            return book
        except StopIteration:
            return "Book not found."

    def remove_book(self, title) -> str:
        book = Library.find_book_by_title(self, title)
        self.books.remove(book)
        return f"Successfully removed {title} from the library."

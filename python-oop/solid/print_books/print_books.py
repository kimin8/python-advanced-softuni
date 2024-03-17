class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class PaperFormatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content[:4]


class Printer:
    @staticmethod
    def get_book(book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book

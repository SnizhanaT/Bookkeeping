from typing import List


class Book:
    def __init__(self, title: str, author: str, genre: str, publication_year: int):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def get_info(self) -> str:
        return f"{self.title} by {self.author}, {self.publication_year} ({self.genre})"


class Shelf:
    def __init__(self, shelf_id: str):
        self.shelf_id = shelf_id
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self) -> List[Book]:
        return self.books

    def remove_book(self, book: Book):
        self.books.remove(book)

    def sort_books_by_title(self):
        self.books.sort(key=lambda book: book.title)


class Room:
    def __init__(self):
        self.shelves: List[Shelf] = []

    def add_shelf(self, shelf: Shelf):
        self.shelves.append(shelf)

    def get_books(self) -> List[Book]:
        all_books = []
        for shelf in self.shelves:
            all_books.extend(shelf.get_books())
        return all_books

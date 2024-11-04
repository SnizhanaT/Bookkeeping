from typing import List, Dict  
from collections import defaultdict
from library import Book, Room, Shelf  


def organize_books_by_category(pile_of_books: List[Book], room: Room):
    genre_to_books: Dict[str, List[Book]] = defaultdict(list)
    
    for book in pile_of_books:
        genre_to_books[book.genre].append(book)

    for genre, books in genre_to_books.items():
        shelf = Shelf(shelf_id=f"Shelf-{genre}")
        for book in books:
            shelf.add_book(book)
        room.add_shelf(shelf)
    print("Books have been organized into shelves by category.")


def sort_books_on_shelves(room: Room):
    for shelf in room.shelves:
        shelf.sort_books_by_title()
    print("Books on each shelf have been sorted by title in ascending order.")

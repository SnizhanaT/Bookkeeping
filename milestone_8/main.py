from library import Book, Room  
from organize_books import organize_books_by_category, sort_books_on_shelves 


pile_of_books = [
    Book(title="The Catcher in the Rye", author="J.D. Salinger", genre="Fiction", publication_year=1951),
    Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", publication_year=1960),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction", publication_year=1925),
    Book(title="A Brief History of Time", author="Stephen Hawking", genre="Science", publication_year=1988),
    Book(title="The Art of Computer Programming", author="Donald Knuth", genre="Programming", publication_year=1968),
    Book(title="Clean Code", author="Robert C. Martin", genre="Programming", publication_year=2008)
]

bob_room = Room()

organize_books_by_category(pile_of_books, bob_room)


sort_books_on_shelves(bob_room)


for shelf in bob_room.shelves:
    print(f"\n{shelf.shelf_id} contains the following books:")
    for book in shelf.get_books():
        print(" -", book.get_info())

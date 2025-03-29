class Book:
    def __init__(self, book_id, book_title, book_author, book_genre):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_genre = book_genre

    def __str__(self):
        return f"{self.book_title} by {self.book_author} ({self.book_genre})"

    def __repr__(self):
        return f"Book(ID: {self.book_id}, Title: {self.book_title}, Author: {self.book_author}, Genre: {self.book_genre})"

class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

class Librarian(User):
    def __init__(self, user_id, user_name, library):
        super().__init__(user_id, user_name)
        self.library = library
    def add_book(self, book):
        self.library.add_book(book)
    def remove_book(self, book_id):
        return self.library.remove_book(book_id)
class Member(User):
    def __init__(self, user_id, user_name, library):
        super().__init__(user_id, user_name)
        self.library = library
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.library.books and book not in self.library.borrowed_books:
            self.borrowed_books.append(book)
            self.library.borrowed_books.append(book)
            self.library.books.remove(book)
            return "Book borrowed successfully!"
        return "Book not available"
       
    def return_book(self, book):
        if book not in self.borrowed_books:
            return "The book was not borrowed"
        self.borrowed_books.remove(book)
        self.library.books.append(book)
        self.library.borrowed_books.remove(book)
        return "Book returned successfully!" 

    def view_borrowed_books(self):
        return self.borrowed_books

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book in self.borrowed_books:
                    return "Book is currently borrowed and cannot be removed."
                self.books.remove(book)
                return f"{book.book_title} removed."
        return "Book not found"
    
    def update_book(self, book_id, new_title, new_author, new_genre):
        for book in self.books:
            if book.book_id == book_id:
                book.book_title = new_title if new_title else book.book_title
                book.book_author = new_author if new_author else book.book_author
                book.book_genre = new_genre if new_genre else book.book_genre
                return f"{book.book_title} updated."
        return "Book not found"
    
    def search_book(self, book_title=None, book_author=None, book_genre=None):
        if not any([book_title, book_genre, book_author]):
            return "No search criteria provided"
        book_title = book_title.lower() if book_title else None
        book_author = book_author.lower() if book_author else None
        book_genre = book_genre.lower() if book_genre else None

        result = [
            book for book in self.books
            if 
                (book_title and book_title in book.book_title.lower()) or
                (book_author and book_author in book.book_author.lower()) or
                (book_genre and book_genre in book.book_genre.lower())
        ]
        return result if result else "No books found matching the criteria provided"

    def display_available_books(self):
        return self.books if self.books else "No books available in the library."


# library = Library()
# book1 = Book(1, "Atomic Habits", "James Clear", "Self-Help")
# book2 = Book(2, "Harry Potter", "J. K. Rowling", "Fantasy")
# book3 = Book(3, "Pride and Prejudice", "Jane Austen", "Fiction")
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# librarian = Librarian(50, "Laiba", library)
# member = Member(51, "Alisha", library)
# print("Avalaible Books:", library.display_available_books())
# print(member.borrow_book(book2))
# print("Available books after borrowing: ", library.display_available_books())
# print(member.return_book(book2))
# print("Available books after returning: ", library.display_available_books())
# print("Search by title: ", library.search_book(book_title="Atomic Habits"))
# print(librarian.remove_book(2))
# print("Available books after removal: ", library.display_available_books())
# print(library.update_book(3, new_title="The art of being alone", new_author="Renuka Gavrani", new_genre="Self-Help"))
# print("Updated book: ", library.search_book(book_author="Renuka Gavrani"))


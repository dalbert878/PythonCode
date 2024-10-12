class Book:
    """Represents a book in the library with title, author, year, and availability status."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True  # Book availability status

    def __str__(self):
        """Returns a string representation of the book."""
        availability = 'Available' if self.available else 'Checked Out'
        return f"{self.title} by {self.author} ({self.year}) - {availability}"


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        self.books = []  # Initialize an empty list to store books

    def add_book(self, book):
        """Adds a new book to the library."""
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, title):
        """Removes a book from the library by its title."""
        book_to_remove = next((book for book in self.books if book.title == title), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Removed: {book_to_remove}")
        else:
            print(f"No book found with title: '{title}'")

    def list_books(self):
        """Lists all books in the library with their availability status."""
        print("\nLibrary Books:")
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def check_out(self, title):
        """Checks out a book from the library if it is available."""
        book_to_check_out = next((book for book in self.books if book.title == title), None)
        if book_to_check_out and book_to_check_out.available:
            book_to_check_out.available = False
            print(f"Checked out: {book_to_check_out}")
        else:
            print(f"Book '{title}' is either not available or does not exist.")

    def return_book(self, title):
        """Returns a checked-out book to the library."""
        book_to_return = next((book for book in self.books if book.title == title), None)
        if book_to_return and not book_to_return.available:
            book_to_return.available = True
            print(f"Returned: {book_to_return}")
        else:
            print(f"Book '{title}' is not checked out or does not exist.")


def main():
    """Main function to demonstrate library management using classes."""
    library = Library()

    # Create some book instances
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("1984", "George Orwell", 1949)
    ]

    # Add books to the library
    for book in books:
        library.add_book(book)

    # List all books in the library
    library.list_books()

    # Check out a book
    library.check_out("1984")

    # List books after checking out one
    library.list_books()

    # Return a book
    library.return_book("1984")

    # List books after returning
    library.list_books()

    # Remove a book
    library.remove_book("The Great Gatsby")

    # List books after removal
    library.list_books()


if __name__ == "__main__":
    main()

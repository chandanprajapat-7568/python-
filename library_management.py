#MADE BY : CHANDAN & BHAVYA CHOUHAN , BCA 3RD GROUP - A2
class Library:
    def __init__(self):
        # Dictionary to store books with book_id as key
        self.books = {}
        # Counter to generate unique book IDs
        self.book_id_counter = 1

    def add_book(self, title, author, genre, year):
        """
        Add a new book to the library
        """
        book_id = f"B{self.book_id_counter:03d}"
        book = {
            'id': book_id,
            'title': title,
            'author': author,
            'genre': genre,
            'year': year
        }
        self.books[book_id] = book
        self.book_id_counter += 1
        print(f"Book '{title}' added successfully with ID: {book_id}")
        return book_id

    def search_book(self, search_term, search_by='title'):
        """
        Search for books by title, author, or genre
        """
        results = []
        for book_id, book in self.books.items():
            if search_by == 'title' and search_term.lower() in book['title'].lower():
                results.append(book)
            elif search_by == 'author' and search_term.lower() in book['author'].lower():
                results.append(book)
            elif search_by == 'genre' and search_term.lower() in book['genre'].lower():
                results.append(book)
            elif search_by == 'id' and search_term == book['id']:
                results.append(book)
        
        return results

    def delete_book(self, book_id):
        """
        Delete a book by its ID
        """
        if book_id in self.books:
            deleted_book = self.books.pop(book_id)
            print(f"Book '{deleted_book['title']}' deleted successfully.")
            return True
        else:
            print(f"Book with ID '{book_id}' not found.")
            return False

    def display_all_books(self):
        """
        Display all books in the library
        """
        if not self.books:
            print("No books in the library.")
            return
        
        print("\n--- All Books in Library ---")
        for book_id, book in self.books.items():
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, "
                  f"Genre: {book['genre']}, Year: {book['year']}")
        print("-----------------------------")

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Book")
    print("2. Search Book")
    print("3. Delete Book")
    print("4. Display All Books")
    print("5. Exit")
    print("="*40)

def get_user_choice():
    """Get and validate user's menu choice"""
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

def handle_add_book(library):
    """Handle adding a new book"""
    print("\n--- Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()

    while True:
        try:
            year = int(input("Enter publication year: "))
            if year > 0:
                break
            else:
                print("Year must be a positive number.")
        except ValueError:
            print("Please enter a valid year.")

    if title and author and genre:
        library.add_book(title, author, genre, year)
    else:
        print("Error: All fields are required!")

def handle_search_book(library):
    """Handle searching for books"""
    print("\n--- Search Books ---")
    print("Search by: 1. Title  2. Author  3. Genre  4. ID")

    while True:
        try:
            search_choice = int(input("Enter search type (1-4): "))
            if search_choice in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

    search_term = input("Enter search term: ").strip()

    if search_choice == 1:
        results = library.search_book(search_term, 'title')
        search_by = 'title'
    elif search_choice == 2:
        results = library.search_book(search_term, 'author')
        search_by = 'author'
    elif search_choice == 3:
        results = library.search_book(search_term, 'genre')
        search_by = 'genre'
    else:  # search_choice == 4
        results = library.search_book(search_term, 'id')
        search_by = 'ID'

    if results:
        print(f"\nFound {len(results)} book(s) matching '{search_term}' by {search_by}:")
        for book in results:
            print(f"  ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, "
                  f"Genre: {book['genre']}, Year: {book['year']}")
    else:
        print(f"No books found matching '{search_term}' by {search_by}.")

def handle_delete_book(library):
    """Handle deleting a book"""
    print("\n--- Delete Book ---")
    book_id = input("Enter book ID to delete (e.g., B001): ").strip()
    if book_id:
        library.delete_book(book_id)
    else:
        print("Book ID cannot be empty.")

def main():
    """Main function to run the library management system"""
    library = Library()
    print("Welcome to the Library Management System!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_add_book(library)
        elif choice == 2:
            handle_search_book(library)
        elif choice == 3:
            handle_delete_book(library)
        elif choice == 4:
            library.display_all_books()
        elif choice == 5:
            print("\nThank you for using the Library Management System!")
            print("Goodbye!")
            break

        # Pause to let user see results before showing menu again
        input("\nPress Enter to continue...")

# Example usage and testing
if __name__ == "__main__":
    main()

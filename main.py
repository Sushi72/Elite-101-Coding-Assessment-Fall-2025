from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def view_books():
    print("Available Books: ")
    for book in library_books:
        if book["available"]:
            print(book["id"] + " - " + book["title"] + " by " + book["author"] + ", " + book["genre"])


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_books():
    matching_books = []
    search_term = input("Please enter an author OR genre to search for books: ").lower()
    for book in library_books:
        if search_term == book["author"].lower() or search_term == book["genre"].lower():
            matching_books.append(book)

    if matching_books:
        print("Matching Books:")
        for book in matching_books:
            print(book["id"] + " - " + book["title"] + " by " + book["author"] + ", " + book["genre"])
    else:
        print("Sorry, we were unable to find this book. Please try again.")
        
    return matching_books 
    

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book():
    id_input = input("Please enter the ID of the book you want to checkout: ").upper()

    for book in library_books:
        if book["id"] == id_input:
            if book["available"]:
                book["available"] = False
                book["due_date"] = str(datetime.today() + timedelta(weeks = 2)).strftime("%Y-%m-%d")
                book["checkouts"] += 1
                print(book["title"] + " successfully checked out.")
            else:
                print(book["title"] + " has already been checked out and is unavaiable.")
            return book

    print("Sorry, we are unable to find this book. Please try again. ")





# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book():
    id_input = input("Please enter the ID of the book you want to return: ").upper()

    for book in library_books:
        if book["id"] == id_input:
            if not book ["available"]:
                book["available"] = True
                book["due_date"] = None
                print(book["title"] + " successfully returned.")
            else:
                print(book["title"] + " cannot be returned.")
            return book
 
    print("Sorry, we are unable to find this book. Please try again. ")


# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def view_overdue_books():
    overdue_books = []
    for book in library_books:
        if not book["available"] and book["due_date"]:
            due_date = datetime.strptime(book["due_date"], "%Y-%m-%d")
            if due_date < datetime.today():
                overdue_books.append(book)

    if overdue_books:
        print("Overdue Books:")
        for book in overdue_books:
            print(book["id"] + " - " + book["title"] + " by " + book["author"] + ", " + book["genre"])
    else:
        print("Sorry, we were unable to find this book. Please try again.")

    return overdue_books



# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.author = data["author"]
        self.genre = data["genre"]
        self.available = data["available"]
        self.due_date = data["due_date"]
        self.checkouts = data["checkouts"]

    def checkout(self):
        if self.available:
            self.available = False
            self.due_date = (datetime.today() + timedelta(weeks = 2)).strftime("%Y-%m-%d")
            self.checkouts += 1
            print(self.title + " successfully checked out.")
        else:
            print(self.title + " has already been checked out and is unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            self.due_date = None
            print(self.title + " successfully returned.")
        else:
            print(self.title + " cannot be returned.")

    def is_overdue(self):
        if not self.available and self.due_date:
            due_date = datetime.strptime(self.due_date, "%Y-%m-%d")
            return due_date < datetime.today()
        return False
    
    def display(self):
        print(self.id + " - " + self.title+ " by " + self.author + ", " + self.genre)

    def menu():
        while True:
            print("Library Menu:")
            print("1. View available books")
            print("2. Search books")
            print("3. Checkout book")
            print("4. Return book")
            print("5. View overdue books")
            print("6. View the top 3 most checked out books")
            print("7. Exit the menu")

    user_selection = input("Please select an option")

    if user_selection == "1":
        print("Available Books:")
        for book in books:
            if book.available:
                book.display()
    elif user_selection == "2":
        
    elif user_selection == "3":
    elif user_selection == "4":
    elif user_selection == "5":
    elif user_selection == "6":
    elif user_selection == "7":
# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    #view_books()
    print("")
    #print(search_books())
    print("")
    #checkout_book()
    #checkout_book()
    print(view_overdue_books())
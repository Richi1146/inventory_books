list_books = []
from book import *
from delete import *
from lend import *
from list import *
from return_book import *




def search_books():
    term = input("Search by title, author, or category: ").strip().lower()

    # Validation: input should not be empty
    if not term:
        print("❌ Please enter a search term.")
        return

    # Search
    results = [
        b for b in list_books
        if term in b["title"].lower()
        or term in b["author"].lower()
        or term in b["category"].lower()
    ]

    # Results
    if not results:
        print("🔎 No matches found.")
        return

    print("\n📚 Search results:")
    for book in results:
        print(f'{book["id"]} | {book["title"]} | {book["author"]} | {book["year"]} | {book["category"]} | {book["state"]}')
        
def show_menu():
    flag = True
    while flag:
        print("\n==== MAIN MENU ====")
        print("1. Register books")
        print("2. List all books")
        print("3. Search for books")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Delete a book")
        print("7. Exit")

        option = input("Choose an option (1-7): ")

        match option:
            case "1":
                print("Option 1: Register books")
                register_book()
            case "2":
                print("Option 2: List all books")
                book_list()
            case "3":
                print("Option 3: Search for books")
                search_books()
            case "4":
                print("Option 4: Borrow a book")
                lend_book()
            case "5":
                print("Option 5: Return a book")
                book_return()
            case "6":
                print("Option 6: Delete a book")
                delete_book()
            case "7":
                print("Exiting the program...")
                flag = False
            case _:
                print("Invalid option. Please try again.")

# Run the menu
if __name__ == '__main__':
    show_menu()

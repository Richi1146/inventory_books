def search_books():
    term = input("Search by title, author, or category: ").strip().lower()

    # Validation: input should not be empty
    if not term:
        print("❌ Please enter a search term.")
        return

    # Validation: input should not contain only spaces or symbols
    if term.replace(" ", "").isnumeric() or not any(c.isalpha() for c in term):
        print("❌ Please enter a valid search term containing letters.")
        return

    # Optional validation: at least 2 useful characters
    if len(term.replace(" ", "")) < 2:
        print("❌ Please enter at least two letters to search.")
        return

    # Search
    results = [
        b for b in book
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
        print(f'{book["id"]} | {book["title"]} | {book["author"]} | {book["year"]} | {book["category"]} | {book["status"]}')


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
                # register_book()
            case "2":
                print("Option 2: List all books")
                # list_books()
            case "3":
                print("Option 3: Search for books")
                # search_books()
            case "4":
                print("Option 4: Borrow a book")
                # borrow_book()
            case "5":
                print("Option 5: Return a book")
                # return_book()
            case "6":
                print("Option 6: Delete a book")
                # delete_book()
            case "7":
                print("Exiting the program...")
                flag = False
            case _:
                print("Invalid option. Please try again.")

# Run the menu
show_menu()
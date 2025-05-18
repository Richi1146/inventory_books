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
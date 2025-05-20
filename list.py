# Funcion para Mostrar todos los libros con todos sus datos,
# y opcion de filtrar entre available y no available,
from menu_search import list_books

def book_list():
    validate = True
    while validate:
        print("1. Show all books.")
        print("2. Filter the availables.")
        print("3. Filter the borroweds.")
        option = input("Enter an option from 1 to 3: ")
        print("-"*50)

        if not list_books:
            print("There are no books available.")
            break
        

        for book in list_books: 
            if option == "1":                                        
                    if book["state"] == "borrowed":
                        print(f"Title: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}, Nombre: {book['loan']['name']}, año: {book['loan']['date']}")
                    elif book["state"] == "available":
                        print(f"Title: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}")
                    validate = False
            
            elif option == "2":
                if book["state"] == "available":
                    print(f"Title: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}")
                    validate = False
            elif option == "3":
                borrowed_books = [b for b in list_books if b["state"] == "borrowed"]
                if not borrowed_books:
                    print("No books available") 
                    print("-"*50)
                    validate = False
                if book['state'] == "borrowed":
                    print(f"Title: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}, Nombre: {book['loan']['name']}, año: {book['loan']['date']}")
                    validate = False

            else: 
                print("Invalid option, you must enter a number from 1-3")
                break
         

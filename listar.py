# Funcion para Mostrar todos los libros con todos sus datos,
# y opcion de filtrar entre disponible y no disponible,
books = [{"title": "book1", "id": "1", "author": "richi", "year": "2025", "category": "fiction", "state": "prestado", "prestamo": {"name": "richi", "year": "2025"}},
        {"title": "book2", "id": "2", "author": "richi2", "year": "2025", "category": "action", "state": "disponible"}]

def list_books():
    validate = True
    while validate:
        print("1. Mostrar todos los libros.")
        print("2. Filtrar los disponibles.")
        print("3. Filtrar los prestados.")
        option = input("Ingresa una opcion de 1 a 3: ")
        print("-"*50)
        

        for book in books: 
            if option == "1":                                        
                    if book["state"] == "prestado":
                        print(f"Titulo1: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}, Nombre: {book['prestamo']['name']}, año: {book['prestamo']['year']}")
                    elif book["state"] == "disponible":
                        print(f"Titulo: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}")
                    validate = False
            
            elif option == "2":
                if book["state"] == "disponible":
                    print(f"Titulo: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}")
                    validate = False
            elif option == "3":
                if book["state"] == "prestado":
                    print(f"Titulo1: {book['title']}, ID: {book['id']}, Author: {book['author']}, Year: {book['year']}, Category: {book['category']}, State: {book['state']}, Nombre: {book['prestamo']['name']}, año: {book['prestamo']['year']}")
                    validate = False
            else: 
                print("Opcion invalida, Debes ingresar un numero de 1-3")
                break

list_books()
import datetime
from menu_search import list_books

def lend_book():

    try:
        id_book = int(input("Enter the ID of the book to be borrowed: "))
    except ValueError:
        print("Invalid ID.")
        return

    # Buscar el book por ID
    for book in list_books:
        if book['id'] == id_book:
            if book['state'] == "borrowed":
                print("The book is already on loan.")
                return
            person = input("name of the person receiving the loan: ").strip()
            
            # Validar que la person no tenga más de 3 préstamos activos
            personal_loans = [l for l in list_books if l.get('loan') and l['loan']['name'] == person]
            if len(personal_loans) >= 3:
                print(f"The person {person} already has 3 books borrowed.")
                return
            loan_date = input("Loan date (YYYY-MM-DD): ").strip()
            # Validar fecha
            try:
                loan_date = datetime.datetime.strptime(loan_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date. Expected format: YYYY-MM-DD.")
                return

            # Prestar el book
            book['state'] = "borrowed"
            book['loan'] = {
                'name': person,
                'date': loan_date.strftime("%Y-%m-%d")
            }
            print(f"book ID {id_book} borrowed to {person}.")
            
            return

    print("book not found.")


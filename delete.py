from menu_search import list_books
def delete_book():
    
    flag = True
    while flag:
    
        if list_books:
            book_delete = input("Enter book to delete: ").strip().lower()
            found = False
            for search in list_books:
            
                if book_delete in search['title'] == book_delete:
                    
                    if search['state'] == "available":
                        found = True
                        question = input("Are you sure you want to delete the book y/n?: ").lower().strip()
                    
                        if question == "y":
                            list_books.remove(search)
                            print("Book to delete successfully")
                            flag = False
                            break
                        elif question == "n":
                            break
                        else:
                            print("enter y/n, please")
                    else:
                        print("The book is currently borrowed")
                        break
            if not found:
                print("Book not found")
                flag = False

        else :
            print("The invetory is empty")
            break

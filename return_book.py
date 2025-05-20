from menu_search import list_books

def book_return():
    
    flag = True
    while flag:
        
        if list_books:
            
            book_to_return = input("what is the book to return ?: ")
            
            found = False
            for search in list_books:
            
                if book_to_return in search['title']:
                    found = True
                    
                    if search['state'] == "borrowed":
                        
                        search['state'] = "available"
                        del search['loan']
                        print(list_books)
                        flag = False
                    else:
                        
                        print("The book is currently avaible ")
                        flag = False
                        
            if not found:
                print("Book not found")
        else :
            print("The invetory is empty")
            break

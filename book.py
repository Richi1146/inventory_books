# Register book
from datetime import datetime
import re


from menu_search import list_books




def validation_author(name):
    
    text = input(name)
    if re.search(r"[#$%&/()=?¡!<>.;,*{}^-_¿|°0-9]",text): 
        print("Enter the name correctly")
        return validation_author(text)
    else :
        return text 
def category():
    
    flag = True
    while flag:
            
        main = input('''
        Enter category :
        1- Fiction
        2- not fiction
        3- childish
        4- Educational
        = ''').lower()
        
        match main:
            
            case "1" | "Fiction":
                category = "fiction"
                return category
            case "2" | "Not Fiction":
                category = "not fiction"
                return category
            case "3" | "childish":
                category = "childish"
                return category
            case "4" | "Educational":
                category = "educational"
                return category
            case _:
                print("Select a option valid")
                             
def register_book ():
    cont = 1
    flag = True
    while flag:
        
        question = input("How many book do you want enter? : ")
        
        if re.search(r"[#$%&/()=?¡!<>.;,*{}^-_¿|°a-zA-Z]",question):
            print("Error X = enter a worth valid")
        else:
            
            while cont < int(question)+1:
                title = str(input("Enter the tittle of book: ")).strip()
                id_book = id(title)
                
                author = validation_author("Enter the author: ").strip()
                    
                year_book = int(input("Enter the year of book: "))
                if 1500 >= year_book <= datetime.today().year :
                        print("The year not is permitted")
                else:
                        category_add = category()
                        state = "available"
                        add_books = {'id':id_book,'title':title,'author':author, 'year': year_book,'category':category_add , 'state' : state  }
                        list_books.append(add_books)
                        cont +=1
                        print(list_books)
        flag = False                
                                         






                
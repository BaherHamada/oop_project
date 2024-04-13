import termcolor
import pyfiglet

class Book:
    id=0
    def __init__(self) -> None:
        Book.id+=1
        
        self.title=str(input("Enter The Book Name : ")).strip().capitalize()
        
        self.author=str(input("Enter The Book Author : ")).strip().capitalize()
        
        res=any(chr.isdigit() for chr in self.author)
        if res==True:
            raise ValueError("Error!!,The author name can't contain [1,2,3,/,*,-,@,...,etc].")
        
        self.genre=str(input("Enter The Book Genre : ")).strip().capitalize()
        
        try:
            self.pub_year=int(input("Enter The Book Publication Year : "))
        except:
            print("Numbers is only allowed!!")
        
#----------------------------------------------------------#
class Library(Book):
    books=[]
    #-------------------------------------------------------------------------------------------#
    def __init__(self) :
        
        name=str(input("Please enter your name : ")).strip().capitalize()
        
        res=any(chr.isdigit() for chr in name)
        
        if res==True:
            raise ValueError("Error,Your name can't contain [1,2,3,/,*,-,@,...,etc].")
        
        print(termcolor.colored(pyfiglet.figlet_format(f"Hello , {name}"),color="green"))
        print("How can I help you ? This is the functions that our Library provid :")
        func="""
        1-Add new book to the library.
        2-Remove a book from the library.
        3-Search for a specific book.
        4-Display the content of the library.
        5-Clear the library.
        """
        
        print(func)
        
        while True:
            reqest=int(input("Enter the the number of the function to go to the next step : "))
            if reqest==1:
                self.add_book()
            elif reqest==2:
                self.remove_book()
            elif reqest==3:
                self.search_book()
            elif reqest==4:
                self.diplay_library()
            elif reqest==5:
                self.clear_lib()    
            more=str(input("Do you want to do anything more :[Yes/No]\n")).strip().capitalize()
            if more=="Yes":
                continue
            elif more=="No":
                print(termcolor.colored(pyfiglet.figlet_format("Thank you to use our App."),color="green"))
                print(termcolor.colored(pyfiglet.figlet_format("By By."),color="green"))
                return
    #-------------------------------------------------------------------------------------------#           
    def add_book(self):
        file=open(r"C:\Users\DELL\OneDrive\Desktop\OOP_Library_Project\library.txt",'a')
        book=Book()
        # file.write("ID      Title       Author      Genre       Publication Year\n")
        file.write(f"Book Title ---> {book.title} || Author ---> {book.author} || Book Genre ---> {book.genre} || Book Publication Year   ---> {book.pub_year}\n")
        self.books.append(book)
        file.close()
    #-------------------------------------------------------------------------------------------#    
    def remove_book(self):
        del_book=str(input("Please enter the name of the book to delete : ")).strip().capitalize()
        with open(r"C:\Users\DELL\OneDrive\Desktop\OOP_Library_Project\library.txt", 'r') as file:
            lines = file.readlines()

        lines = [line for line in lines if not line.startswith(f"Book Title ---> {del_book}")]

        with open(r"C:\Users\DELL\OneDrive\Desktop\OOP_Library_Project\library.txt", 'w') as file:
            file.writelines(lines)
        file.close()
    #-------------------------------------------------------------------------------------------#    
    def search_book(self):
        find_book=str(input("Please enter the name of the book you search for : ")).strip().capitalize()
        file=open(r"C:\Users\DELL\OneDrive\Desktop\OOP_Library_Project\library.txt", 'r') 
        for book in file:
            if book.startswith(f"Book Title ---> {find_book}"):
                print("The Book is exist in the library.")
                return
        print("The Book dosn't exist!!")    
    #-------------------------------------------------------------------------------------------#
    def diplay_library(self):
        f=open(r"C:\Users\DELL\OneDrive\Desktop\OOP_Library_Project\library.txt",'r')
        print(f.read())
        f.close()
    #-------------------------------------------------------------------------------------------#
    def clear_lib(self):
        file=open(r"C:\Users\DELL\OneDrive\Desktop\OOP_Library_Project\library.txt",'w')
        file.write('')
        print(termcolor.colored("Done.",color="green"))
    
    
Baher=Library()

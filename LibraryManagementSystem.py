class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

  
    def addBook(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f"'{book_name}' ko Library mein add kar diya gaya hai! ")

    
    def showInfo(self):
        print("\n" + "="*30)
        print(f"Total Books ki ginti: {self.no_of_books}")
        
        
        
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")
        print("="*30 + "\n")





my_library = Library()


my_library.addBook("Harry Potter")
my_library.addBook("Rich Dad Poor Dad")
my_library.addBook("Think and Grow Rich")


my_library.showInfo()

if len(my_library.books) == my_library.no_of_books:
    print("Mubarak ho! Aapka code ekdum sahi hai aur dono ginti barabar hain! ")
else:
    print("Oops! Ginti mein kuch gadbad hai. ")

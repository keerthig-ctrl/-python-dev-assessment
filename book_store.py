class Book:
    def__init__(self,title,author,isbn,publication_year)
       self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2025
        return current_year - self.publication_year
    
    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"
    

if __name__=="__main__":
    book1 = Book("Python Basics", "John Smith", "1234567890", 2020)
    book2 = Book("Data Structures", "Jane Doe","0987654321",2018)

    print(book1.get_summary())
    print("Age:",book1.get_age())
    print(book2.get_summary())
    print("Age:",book2.get_age())

    

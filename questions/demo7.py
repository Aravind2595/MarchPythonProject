#3Create a Book class with instance Library_name, book_name, author, pages?

class Book:
    def set(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def print(self):
        print("Library:",self.library_name)
        print("Book:",self.book_name)
        print("author:",self.author)
        print("pages:",self.pages)
bo=Book()
bo.set("Vayalr Vayanashala","2 States : The story of my marriage","Chetan Bhagat",321)
bo.print()
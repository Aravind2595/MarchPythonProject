#book name,author,pages
class Book:
    def setval(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
        print("Book Name:",self.name)
        print("Author Name:",self.author)
        print("Pages:",self.pages)
    def __str__(self):
        return self.name+self.author+str(self.pages)
bk=Book()
bk.setval("2 states:the story of my marriage","Chetan Bhagat",321)
print(bk)

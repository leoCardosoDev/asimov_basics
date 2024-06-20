class Book(object):
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return "Title: %s, Author: %s, Pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book is destroyed')


book = Book('Curso de Python', 'Leo Silva', 159)
# Metodos especial
print(book)
print(len(book))
del book

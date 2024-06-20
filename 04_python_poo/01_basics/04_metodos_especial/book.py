class Book(object):
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages


book = Book('Curso de Python', 'Leo Silva', 159)

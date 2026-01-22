class Book:
    
    def __init__(self, title, author, is_read=False):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print("Kitob o'qilgan deb belgilandi")

    def status(self):
        if self.is_read:
            print("O'qilgan")
        else:
            print("O'qilmagan")

book1 = Book("Atomic Habits", "James Clear")

book1.status()
book1.mark_as_read()
book1.status()

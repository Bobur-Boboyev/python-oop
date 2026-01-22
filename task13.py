class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
        print(f"'{self.title}' o'qilgan deb belgilandi")

    def status(self):
        if self.is_read:
            print(f"{self.title}: O'qilgan")
        else:
            print(f"{self.title}: O'qilmagan")

book1 = Book("Metamorphosis", "Frans Kafka")
book2 = Book("Clean Code", "Robert C. Martin")
book3 = Book("1984", "George Orwell")
book4 = Book("Atomic Habits", "James Clear")

book1.mark_as_read()
book3.mark_as_read()

book1.status()
book2.status()
book3.status()
book4.status()


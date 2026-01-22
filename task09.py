class User:
    
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        self.is_active = True
        print(f"{self.username} foydalanuvchisi faollashtirildi")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} foydalanuvchisi bloklandi")

user1 = User("ali", "ali@example.com", False)

user1.activate()
user1.deactivate()

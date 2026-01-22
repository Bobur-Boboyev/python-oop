class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance} so'm")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.balance} so'm")
        else:
            print("Balansda yetarli mablag' yo'q")

    
b = BankAccount('Bobur', 1000)

print(b.deposit(100000))
print(b.withdraw(100000000))
print(b.withdraw(100))
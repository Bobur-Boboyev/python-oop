class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}: {amount} so'm qo'shildi")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner}: {amount} so'm yechildi")
        else:
            print(f"{self.owner}: Balans yetarli emas")

    def show_balance(self):
        print(f"{self.owner} hisobidagi balans: {self.balance} so'm")

account1 = BankAccount("Ali", 500_000)
account2 = BankAccount("Vali", 300_000)
account3 = BankAccount("Sara", 1_000_000)

account1.deposit(200_000)
account1.withdraw(100_000)

account2.deposit(50_000)
account2.withdraw(400_000)

account3.withdraw(300_000)
account3.deposit(150_000)

account1.show_balance()
account2.show_balance()
account3.show_balance()
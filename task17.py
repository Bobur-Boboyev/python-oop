class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} hisobidagi balans: {self.balance} so'm")

    def get_balance(self):
        return self.balance
    

acc1 = BankAccount("Ali", 500_000)
acc2 = BankAccount("Vali", 300_000)
acc3 = BankAccount("Sara", 1_000_000)
acc4 = BankAccount("Olim", 750_000)
acc5 = BankAccount("Nodira", 600_000)

accounts = [acc1, acc2, acc3, acc4, acc5]

total_balance = 0
for account in accounts:
    total_balance += account.get_balance()

print(f"Bankdagi jami balans: {total_balance} so'm")


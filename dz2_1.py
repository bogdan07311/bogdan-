class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит: {amount}. Новий баланс: {self.balance}.")
        else:
            print("Сума депозиту повинна бути додатною.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів для зняття.")
        elif amount <= 0:
            print("Сума зняття повинна бути додатною.")
        else:
            self.balance -= amount
            print(f"Зняття: {amount}. Новий баланс: {self.balance}.")
account = BankAccount("UA123456789", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
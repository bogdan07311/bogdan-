class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        """
        Ініціалізація банківського рахунку.

        :param owner_name: Ім'я власника рахунку
        :param account_number: Номер рахунку
        :param balance: Поточний баланс рахунку (за замовчуванням 0)
        """
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Поповнити рахунок."""
        if amount > 0:
            self.balance += amount
            print(f"Рахунок {self.account_number}: поповнено на {amount} грн. Поточний баланс: {self.balance} грн.")
        else:
            print("Сума поповнення повинна бути більшою за нуль.")

    def withdraw(self, amount):
        """Зняти кошти з рахунку."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Рахунок {self.account_number}: знято {amount} грн. Поточний баланс: {self.balance} грн.")
        else:
            print("Недостатньо коштів або неправильна сума для зняття.")

    def get_balance(self):
        """Отримати поточний баланс рахунку."""
        return self.balance
class Bank:
    def __init__(self):
        """Ініціалізація банку."""
        self.accounts = []
    def transfer(self, from_account, to_account, amount):
        """Переказ коштів між рахунками."""
        if from_account.get_balance() >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(
                f"Переказ на {amount} грн. з рахунку {from_account.account_number} на рахунок {to_account.account_number}.")
        else:
            print("Недостатньо коштів для переказу.")

    def show_all_accounts(self):
        """Вивести інформацію про всі рахунки в банку."""
        if self.accounts:
            print("Інформація про всі рахунки:")
            for account in self.accounts:
                print(account)
        else:
            print("В банку немає рахунків.")
bank = Bank()
account1 = bank.create_account("Олександр")
account2 = bank.create_account("Марія")
account1.deposit(5000)
account2.deposit(2000)
account1.withdraw(1000)
account2.withdraw(3000)
bank.transfer(account1, account2, 1500)
bank.show_all_accounts()

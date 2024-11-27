class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates
    def convert(self, amount, from_currency, to_currency):
        """Конвертує валюту з однієї в іншу"""
        if from_currency == to_currency:
            return amount
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Невідомі валюти.")
        base_amount = amount / self.exchange_rates[from_currency]
        converted_amount = base_amount * self.exchange_rates[to_currency]
        return converted_amount
exchange_rates = {
    'UAH': 0.027,
    'USD': 1.0,
    'EUR': 0.93,
    'GBP': 0.81,
}
def main():
    print("Ласкаво просимо в конвертацію валют!")
    amount = float(input("Введіть кількість вашої валюти: "))
    from_currency = input("Введіть вашу валюту: ").upper()
    to_currency = input("Введіть валюту, в яку потрібно конвертувати: ").upper()
    converter = CurrencyConverter(exchange_rates)
    try:
        converted_amount = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} дорівнює {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()


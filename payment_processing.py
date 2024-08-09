class PaymentProcessor:
    def __init__(self):
        self.current_balance = 0.0

    def validate_payment(self, price, amount):
        return amount >= price

    def complete_transaction(self, amount):
        self.current_balance += amount

    def get_balance(self):
        return self.current_balance

# Strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete strategy classes
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} via Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} via PayPal")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} via Bank Transfer")

# Context class
class ShoppingCart:
    def __init__(self, payment_strategy):
        self._items = []
        self._payment_strategy = payment_strategy

    def add_item(self, item):
        self._items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self._items)

    def checkout(self):
        total_amount = self.calculate_total()
        self._payment_strategy.pay(total_amount)

# Client code
if __name__ == "__main__":
    # Create payment strategies
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    bank_transfer_payment = BankTransferPayment()

    # Create shopping carts with different payment strategies
    cart1 = ShoppingCart(credit_card_payment)
    cart2 = ShoppingCart(paypal_payment)
    cart3 = ShoppingCart(bank_transfer_payment)

    # Add items to shopping carts
    cart1.add_item({"name": "Item 1", "price": 100})
    cart2.add_item({"name": "Item 2", "price": 200})
    cart3.add_item({"name": "Item 3", "price": 300})

    # Checkout
    cart1.checkout()  # Output: Paying 100 via Credit Card
    cart2.checkout()  # Output: Paying 200 via PayPal
    cart3.checkout()  # Output: Paying 300 via Bank Transfer

class UserInterface:
    def __init__(self, inventory, payment_processor):
        self.inventory = inventory
        self.payment_processor = payment_processor

    def display_products(self):
        for product in self.inventory.get_products():
            print(f"{product.id}: {product.name} - ${product.price}")

    def select_product(self, product_id):
        product = self.inventory.get_product_by_id(product_id)
        if product:
            return product
        else:
            print("Product not available.")
            return None

    def process_payment(self, product):
        amount = float(input("Insert cash amount: "))
        if self.payment_processor.validate_payment(product.price, amount):
            self.payment_processor.complete_transaction(product.price)
            self.inventory.update_stock(product)
            print("Transaction successful. Dispensing product...")
            return True
        else:
            print("Insufficient funds or invalid payment.")
            return False

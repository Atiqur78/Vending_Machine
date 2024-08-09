
from inventory_management import   *
from payment_processing import *
from user_interface import *
from dispensing import *
from security import *

class VendingMachine:
    def __init__(self):
        self.inventory = InventoryManagement()
        self.payment_processor = PaymentProcessor()
        self.user_interface = UserInterface(self.inventory, self.payment_processor)
        self.dispensing_mechanism = DispensingMechanism()
        self.security_measures = SecurityMeasures()

    def add_product_to_inventory(self, product):
        self.inventory.add_product(product)

    def start(self):
        while True:
            self.user_interface.display_products()
            product_id = int(input("Select product ID: "))
            product = self.user_interface.select_product(product_id)
            if product:
                if self.user_interface.process_payment(product):
                    self.dispensing_mechanism.dispense(product)
                    self.security_measures.log_transaction(f"Dispensed {product.name} for ${product.price}")
                else:
                    print("Transaction failed.")
            else:
                print("Invalid product selection.")


if __name__ == "__main__":
    vm = VendingMachine()
    vm.add_product_to_inventory(Product(1, "Coke", 1.50, 10))
    vm.add_product_to_inventory(Product(2, "Pepsi", 1.50, 10))
    vm.add_product_to_inventory(Product(3, "Water", 1.00, 20))
    vm.start()

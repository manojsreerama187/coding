class Product:
    def __init__(self,product_id,name,price,quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
class Inventory:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        for p in self.products:
            if p.product_id == product.product_id:
                p.quantity += product.quantity
                return
        self.products.append(product)
    def remove_product(self,product_id):
        self.products=[p for p in self.products if p.product_id != product_id]
    def get_product(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                return f" Product: {p.name}, price:{p.price}, quantity:{p.quantity}"
        return None
    def list_products(self):
        return [f"Prodcut:{p.name},Price:{p.price},Quantity:{p.quantity}" for p in self.products]
    def total_values(self):
                return sum(p.price*p.quantity for p in self.products)
    def reorder_list(self,threshold):
        return  [p.name for p  in self.products if p.quantity < threshold]
    
    
def main():
    # Create an inventory
    inventory = Inventory()
    
    # Add products to the inventory
    product1 = Product(1, "Widget A", 9.99, 50)
    product2 = Product(2, "Widget B", 14.99, 30)
    product3 = Product(3, "Widget C", 12.50, 25)
    product4 = Product(4, "Widget D", 19.99, 40)
    
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)
    inventory.add_product(product4)
    
    # Remove a product from the inventory
    inventory.remove_product(3)
    # Retrieve product details by product_id
    product2_details = inventory.get_product(2)
    print(product2_details)
    
    # List all products in the inventory
    all_products = inventory.list_products()
    for product in all_products:
        print(product)
    # Calculate and print the total inventory value
    total_value = inventory.total_values()
    print("Total Inventory Value: ${:.2f}".format(total_value))
    # List products that need to be reordered
    reorder_list = inventory.reorder_list(40)
    print("Products to Reorder:")
    for product in reorder_list:
        print(product)
if __name__ == "__main__":
    main()        

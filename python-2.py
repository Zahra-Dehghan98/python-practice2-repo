# PRACTICE 2: make console for simulation of shopping from webstore.

#MINI STORE MANAGEMENT SYSTEM 

#class product
class Product:
    """displaying product information in the store"""

    def __init__(self, name:str, price:float, stock:int):
        self.name = name
        self.price = price
        self.stock = stock

#class store
class Store:
    """This class is going to manage the list of all products (adding, displaying, and searching)"""

    def __init__(self):
        """__init__: Initialize a new product"""
        self.products = []

    def add_product(self, name:str, price:float, stock:int):
        """add_product: Add a new product to the store inventory"""
        new_product = Product(name, price, stock)
        self.products.append(new_product)
    
    def list_products(self):
        """list_product: Display all available products in the store."""
        if not self.products:
            print("No products available yet.")
        else:
            for product in self.products:
                print(product.name, product.price, product.stock)
    
    def find_product(self, name:str):
        """find_product: Search for a product in the store by name."""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
            continue
        return None

#class CartItem
class CartItem:
    """Keeping information for each item in the cart with the purchased quantity"""
    def __init__(self, product:Product, quantity:int):
        self.product = product
        self.quantity = quantity

#class Cart
class Cart:
    """This class maintains a list of CartItem objects and performs operations such as adding, removing, and calculating the total price."""
    def __init__(self):
        self.items = []
    def add_to_cart(self, product:Product, quantity:int):
        """add_to_cart: Add a product to the shopping cart with specified quantity"""
        for item in self.items:
            if item.product.name.lower() == product.name.lower():
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    
    def remove_from_cart(self, product_name):
        """remove_from_cart: Remove a product from the shopping cart by product name"""
        for item in self.items:
            if item.product.name == product_name:
                item.product.stock += item.quantity
                self.items.remove(item)
                return True
        return False
    
    def view_cart(self):
        """view_cart: Display all items currently in the shopping cart"""
        if not self.items:
            print("your cart is empty")
        else:
            for item in self.items:
                print(f"your cart:{item.product.name}, {item.quantity}")
   
    def total_price(self):
        """total_price: Calculate the total price of all items in the shopping cart"""
        total_price = 0
        for item in self.items:
            total_price += item.product.price * item.quantity
        return total_price
    
store = Store()
customer_cart = Cart()

#portable store manager or customer
while True:   
    choice = input("please select your role:")
    if choice == "1":
        username = input("please enter your username:")
        password = input("please enter your password:")
        if username == "admin" and password == "1234":
            print("Login successful! Welcome, Manager.")
        
            while True:
                product_name = input("please enter product name:")
                if product_name != "done":
                    try:
                        product_price = float(input("please enter product price:"))
                    except ValueError:
                        print("please enter a valid price")
                        continue
                    try:
                        product_stock = int(input("please enter product stock quantity:"))
                    except ValueError:
                        print("please enter a valid number")
                        continue
                    store.add_product(product_name, product_price, product_stock)
                    print(f"product added: {product_name}, {product_price}, {product_stock}")
                    continue
                else:
                    break
        else:
            print("Login failed! Please try again or return to main menu.")
            continue
    
        
    elif choice == "2":
        print("Hello, dear customer!")
        while True:
            print("Available Products:\t")
            store.list_products()
            menu = {
                    "1": "Add to cart",
                    "2": "Remove from cart",
                    "3": "View cart",
                    "4": "Total price",
                    "5": "Back to main menu"
            }
            for key, value in menu.items():
                print(f"{key}. {value}")
            choice_2 = input("please enter your choice:")
            if choice_2 == "1":
                product_name = input("please enter product name:")
                try:
                    quantity =int(input("please enter quantity:"))
                except ValueError:
                    print("please enter a valid number")
                    continue
                product = store.find_product(product_name)
                if product is not None:
                    if quantity <= product.stock:
                        customer_cart.add_to_cart(product, quantity)
                        product.stock -= quantity
                        print(f" Added {quantity} x {product.name} to cart")
                    else:
                        print("Not enough stock")
                else:
                    print("Product not found")  

            elif choice_2 == "2":
                product_name = input("please enter product name:")
                product = store.find_product(product_name)
                if customer_cart.remove_from_cart(product_name):
                    print(f"{product_name} removed.")
                    if product:
                        print(f"product_stock: {product.stock}")
                    
                else:
                    print(f"{product_name} not found in your cart.")

                
            elif choice_2 == "3":
                print("Your Cart:")
                customer_cart.view_cart()   

            elif choice_2 == "4":
                print(f"total price:{customer_cart.total_price()}")
            
            elif choice_2 == "5":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice! Please enter 1-5")
    else:
        print("Goodbye! See you next time.")
        break    




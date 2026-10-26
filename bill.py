from functools import reduce
import time

# Decorator that prints how long a function takes to run.
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")
        return result
    return wrapper

# Product prices:
products = {
    "Book" : 300,
    "Pen" : 50,
    "Bag" : 1200
}

# Returns the price of one product multiplied by its quantity.
def product_total(name , qty):
    price = products[name]
    return price * qty

# Takes one order like ("Pen", 3) and returns its total price.
def product_order_total(order):
    name , qty = order
    return product_total(name , qty)

# Returns the discount amount: 20% for 2000 or more, 10% for 500 or more, otherwise 0.
def product_discount(total):
    if total >= 2000:
        discount_rate = 20 / 100
    elif total >= 500:
        discount_rate = 10 / 100
    else:
        discount_rate = 0

    return total * discount_rate

# Adds two numbers. It is used by reduce() to sum a list. 
def add(a,b):
    return a + b

# Returns True if the total price of an order is 500 or more.
def is_big_order(order):
    name , qty = order
    return product_total(name, qty) >= 500

# Each order is a pair: (product name, quantity).
product_order = [("Pen" , 3) , ("Book", 3) ,   ("Bag" , 2) ]

# Prints the full bill: each line, big orders, biggest order, total, discount and final price.
@timer
def show_bill(orders):
    line_totals = list(map(product_order_total ,orders ))
    bill = reduce(add , line_totals)
    for number , order in enumerate(orders, start=1):
        name , qty = order
        amount = product_total(name , qty) 
        print(f"{number}. {name} X {qty} = {amount}") 

    big = list(filter(is_big_order , orders))
    print(f"Big orders: {big}")
    print(f"Biggest order: {max(orders , key=product_order_total)}")
    print(f"Total price: {bill}")
    discount = product_discount(bill)
    print(f"Discount: {discount} Final price: {bill - discount}")

show_bill(product_order)
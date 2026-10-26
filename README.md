# Shop Bill Calculator

A small Python program that turns a customer's order into a clear shop bill. It is a practice project that I built to combine the Python concepts I am learning.

## What it does

Given a list of orders (product name and quantity), the program:

- calculates the price of each order line
- prints a numbered bill
- finds the big orders (500 or more) and the single biggest order
- adds up the total and applies a discount (20% for 2000 or more, 10% for 500 or more)
- prints the final price
- shows how long the bill took to produce

## Example output

```
1. Pen X 3 = 150
2. Book X 3 = 900
3. Bag X 2 = 2400
Big orders: [('Book', 3), ('Bag', 2)]
Biggest order: ('Bag', 2)
Total price: 3450
Discount: 690.0 Final price: 2760.0
Time taken: 0.00 seconds
```

## How to run

1. Install Python 3.
2. Download `bill.py`.
3. Open a terminal in the same folder and run:

```
python bill.py
```

## How it is built

1. **Data:** prices are stored in a dictionary, and the customer's order is a list of `(product, quantity)` tuples.
2. **Small functions:** each function does one job: the price of one line, the discount, whether an order is big.
3. **Bill steps:** `map()` calculates every line total, `reduce()` adds them up, `filter()` finds big orders, `enumerate()` numbers the lines, and `max()` finds the biggest order.
4. **Timing:** a decorator (`@timer`) measures how long the bill takes without changing the bill code.

## Python concepts used

| Feature | Concept |
|---|---|
| Price list | dictionary |
| Order list | list of tuples |
| Price of one order | functions, tuple unpacking |
| Total of all orders | `map()` and `reduce()` |
| Big orders | `filter()` |
| Numbered bill | `enumerate()` |
| Biggest order | `max()` with `key=` |
| Discount rules | `if / elif / else` |
| Timing the bill | decorator (`@timer`) |
| Output lines | f-strings |

## Author

Raza Hussain
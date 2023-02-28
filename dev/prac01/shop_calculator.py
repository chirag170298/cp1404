""" Program to calculate total price for different number of items. """

DISCOUNT = 0.1

quantity = int(input("Number of items: "))

while quantity < 0:
    print("Invalid number of items.")
    quantity = int(input("Number of items: "))

total_price = 0
for prices in range(quantity):
    price = float(input("Price of item: $"))
    total_price += price

if total_price > 100:
    total_price -= (total_price * DISCOUNT)

print(f"Total price for {quantity} items is ${total_price:.2f}")

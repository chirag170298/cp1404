"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MAX_BONUS = 0.15
MIN_BONUS = 0.1

sales = float(input("Enter sales: $"))
bonus = 0
while sales >= 0:
    if sales >= 1000:
        bonus = MAX_BONUS * sales
    else:
        bonus = MIN_BONUS * sales
    print("You get bonus of $", bonus)
    sales = float(input("Enter sales: $"))



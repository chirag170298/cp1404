"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
a1. When the input will be other than an integer number the ValueError will occur.

2. When will a ZeroDivisionError occur?
a2. When the denominator written 0 the ZeroDivisionError occur.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
a3. Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can't be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

# except ZeroDivisionError:
#    print("Cannot divide by zero!")
print("Finished.")

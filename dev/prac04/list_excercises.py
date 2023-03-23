""" part a """

QUANTITY_OF_NUMBERS = 5

numbers = []
for i in range(QUANTITY_OF_NUMBERS):
    number = int(input("Number: "))
    numbers.append(number)
print("The first number is ", numbers[0])
print("The last number is ", numbers[-1])
print("The smallest number is ", min(numbers))
print("The largest number is ", max(numbers))
print("The average of the numbers is ", sum(numbers) / len(numbers))

""" part b. """

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter Username: ")
if username in usernames:
    print("Access Granted.")
else:
    print("Access denied.")

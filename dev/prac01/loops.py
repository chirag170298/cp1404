""" Program to display all the odd numbers between
1 and 20 with a space between each one."""

for i in range(1, 21, 2):
    print(i, end=' ')
print()


""" a. Program to count 10s from 0 to 100."""

for i in range(0, 101, 10):
    print(i, end=' ')
print()


""" b. Program to count down from 20 to 1."""

for i in range(20, 0, -1):
    print(i, end=' ')
print()


""" c. Program that ask the user for a number, then print that many stars"""

stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end='')
print()


""" d. Program that print n lines of increasing stars. """

stars = int(input("Number of stars: "))
for i in range(0, stars):
    for j in range(0, i+1):
        print("*", end='')
    print("\r")
print()

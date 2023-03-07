""" Program to check if passwords meet the criteria or not."""


LENGTH = 6


def main():
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Add Password: ")
    while len(password) < LENGTH:
        print("Password too short.")
        password = input("Add Password: ")
    return password


main()



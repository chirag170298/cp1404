""" program that stores users' emails (unique keys) and names (values) in a dictionary. """


def main():
    emails_to_names = {}
    email = input("Email: ")
    while email != "":
        if email in emails_to_names:
            email = input("Email: ")
            continue
        name = get_name_from_mail(email)
        choice = input(f"Is your name {name}? y/n  ").lower()
        if choice == "y" or choice == "yes":
            emails_to_names[email] = name
        elif choice == "n" or choice == "no":
            name = input("Name: ").title()
            emails_to_names[email] = name
        else:
            print("Invalid Choice")
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def get_name_from_mail(email):
    """ extract name from mail."""
    parts = email.split("@")
    full_name = parts[0].split(".")
    name = " ".join([name.title() for name in full_name])
    return name


main()

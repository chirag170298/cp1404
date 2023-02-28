""" Menu Program """

name = input("Enter name: ")
print("(H)ello \n(G)oodbye \n(Q)uit")
choice = input(">>>").upper()
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print("(H)ello \n(G)oodbye \n(Q)uit")
    choice = input(">>>").upper()
print("Finished.")

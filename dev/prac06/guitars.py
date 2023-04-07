""" The client program"""

from dev.prac06.guitar import Guitar


def main():
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar1 = Guitar(name, year, cost)
        guitars.append(guitar1)
        print(guitar1, "added.")
        name = input("\nName: ").title()

    print("\n...snip...\n")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()

from dev.prac06.guitar import Guitar

guitars = []

with open("guitars.csv", "r") as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)

guitar_name = input("Guitar Name: ").title()
while guitar_name != "":
    guitar_year = int(input("Guitar Year: "))
    guitar_cost = float(input("Guitar Cost: "))
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar)
    guitar_name = input("Guitar Name: ").title()

guitars.sort()

for guitar in guitars:
    print(guitar)

with open("guitars.csv", "w") as out_file:
    for guitar in guitars:
        print(",".join([guitar.name, str(guitar.year), str(guitar.cost)]), file=out_file)

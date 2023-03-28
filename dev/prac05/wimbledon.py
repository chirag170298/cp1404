"""
program to read this file, process the data and display processed information.
the champions and how many times they have won.
the countries of the champions in alphabetical order.
"""


def main():
    filename = "wimbledon.csv"
    champion_to_count = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            text = line.split(',')
            champions = text[2].split("\n")
            add_name_and_count(champion_to_count, champions)
            countries.add(text[1])
    display_name_and_count(champion_to_count)
    display_winning_countries(countries)


def add_name_and_count(champion_to_count, champions):
    """ add champion name and how many times they won in dictionary."""
    for champion in champions:
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1


def display_winning_countries(countries):
    """display countries of the champions in alphabetical order."""
    countries = sorted(countries)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def display_name_and_count(champion_to_count):
    """display champions and how many times they have won"""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion}  {count}")


main()

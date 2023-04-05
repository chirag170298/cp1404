"""
Travel Tracker 1.0
Name: Chirag Verma
Date started: 31/03/2023
GitHub URL: https://github.com/chirag170298/cp1404/tree/master/ChiragVermaA1
"""

import random

FILENAME = "places.csv"
MENU = "Menu: \n" \
       "L - List places \n" \
       "R - Recommend random places \n" \
       "A - Add new place \n" \
       "M - Mark a place as visited \n" \
       "Q - Quit"


def main():
    print("Travel Tracker 1.0 - by Chirag Verma")
    places = load_data()
    print(f"{len(places)} places loaded from {FILENAME}")
    print(MENU)
    choice = get_valid_input(">>> ").upper()
    while choice != 'Q':
        places.sort(key=lambda place: (place[3], int(place[2])))  # Sort list by visited status then by priority
        unvisited_places = [place for place in places if place[3] == 'n']
        if choice == 'L':
            display_list_of_places(places)
        elif choice == 'R':
            if len(unvisited_places) == 0:
                print("No places left to visit!")
            else:
                random_place_generator(unvisited_places)
        elif choice == 'A':
            add_new_place(places)
        elif choice == 'M':
            if len(unvisited_places) == 0:
                print("No unvisited places")
            else:
                display_list_of_places(places)
                mark_place_visited(places)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = get_valid_input(">>> ").upper()

    print(f"{len(places)} places saved to {FILENAME}")
    print("Have a nice day :)")
    save_data(places)


def save_data(places):
    """Overwrite/save list places in file. """
    with open("places.csv", "w") as out_file:
        for place in places:
            print(",".join(place), file=out_file)


def add_new_place(places):
    """Add a new place to a list and by default mark them as unvisited."""
    name = get_valid_input("Name: ").title()
    while not name.isalpha():  # will get a valid string input from user
        print("Invalid input; enter a valid text")
        name = get_valid_input("Name: ").title()
    country = get_valid_input("Country: ").title()
    while not country.isalpha():
        print("Invalid input; enter a valid text")
        country = get_valid_input("Country: ").title()
    priority = get_valid_input("Priority: ")
    while not priority.isdigit():  # will get a valid int input from user
        print("Invalid input; enter a valid number")
        priority = get_valid_input("Priority: ")
    places.append([name, country, priority, "n"])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def get_valid_input(prompt):
    """Get some input from a user."""
    value = input(prompt)
    while value == "":
        print("Input cannot be blank")
        value = input(prompt)
    return value


def mark_place_visited(places):
    """Validate user input and mark the user choose place visited if it is unvisited."""
    print("Enter the number of a place to mark as visited")
    mark_number = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            mark_number = int(get_valid_input(">>> "))
            if mark_number <= 0:
                print("Number must be > 0")
            elif mark_number > len(places):
                print("Invalid place number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    if places[mark_number - 1][3] == 'v':
        print(f"You have already visited {places[mark_number - 1][0]}")
    else:
        places[mark_number - 1][3] = 'v'
        print(f"{places[mark_number - 1][0]} in {places[mark_number - 1][1]} visited")


def random_place_generator(unvisited_places):
    """Randomly recommend a place from unvisited places."""
    randon_choice = random.choice(unvisited_places)
    print("Not sure where to visit next?")
    print("How about... {} in {}?".format(*randon_choice))


def load_data():
    """Load and split data from FILENAME and store it into list."""
    in_file = open(FILENAME, "r")
    places = []
    for line in in_file:
        text = line[:-1].split(",")  # [-1] is for leave \n at the end of each line
        places.append(text)
    in_file.close()
    return places


def display_list_of_places(places):
    """Display the list in a proper format and place an asterisk sign in front of unvisited places."""
    max_len_name = max(len(place[0]) for place in places)
    max_len_country = max(len(place[1]) for place in places)
    unvisited_count = 0
    for i, place in enumerate(places, 1):
        name, country, priority, is_visit = place
        if place[3] == 'n':
            mark = "*"
            unvisited_count += 1
        else:
            mark = " "
        print(f"{mark}{i}. {name:<{max_len_name}} in {country:<{max_len_country}}  {priority:>2} ")
    if unvisited_count == 0:
        print(f"{len(places)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(places)} places. You still want to visit {unvisited_count} places")


if __name__ == '__main__':
    main()

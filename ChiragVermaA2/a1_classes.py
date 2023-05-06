"""
Modified version of assignment 1 so that it uses Place class
GitHub URL: https://github.com/chirag170298/cp1404/tree/master/ChiragVermaA2
"""

from place import Place

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
    # print(places)
    print(f"{len(places)} places loaded from {FILENAME}")
    print(MENU)
    choice = get_valid_input(">>> ").upper()
    while choice != 'Q':
        places = sorted(places, key=lambda x: (x.is_visited, int(x.priority)))
        unvisited_places = [place for place in places if not place.is_visited]
        # print(places)
        # print(unvisited_places)
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
            visited_status = "v" if place.is_visited else "n"
            print(f"{place.name},{place.country},{place.priority},{visited_status}", file=out_file)


def add_new_place(places):
    """Add a new place to a list and by default mark them as unvisited."""
    name = get_valid_input("Name: ").title()
    name = get_string(name, "Name: ")
    country = get_valid_input("Country: ").title()
    country = get_string(country, "Country: ")
    priority = get_valid_input("Priority: ")
    while not priority.isdigit():  # will get a valid int input from user
        print("Invalid input; enter a valid number")
        priority = get_valid_input("Priority: ")
    places.append(Place(name, country, priority, False))
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def get_string(variable, prompt):
    """get only string as input from user"""
    while not variable.isalpha():
        print("Invalid input; enter a valid text")
        variable = get_valid_input(prompt).title()
    return variable


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
    if places[mark_number - 1].is_visited:
        print(f"You have already visited {places[mark_number - 1].name}")
    else:
        places[mark_number - 1].mark_visited()
        print(f"{places[mark_number - 1].name} in {places[mark_number - 1].country} visited")


def random_place_generator(unvisited_places):
    """Randomly recommend a place from unvisited places."""
    randon_choice = random.choice(unvisited_places)
    print(randon_choice)
    print("Not sure where to visit next?")
    print(f"How about... {randon_choice.name} in {randon_choice.country}?")


def load_data():
    """Load and split data from FILENAME and store it into list."""
    in_file = open(FILENAME, "r")
    places = []
    for line in in_file:
        text = line[:-1].split(",")  # [-1] is for leave \n at the end of each line
        is_visited = True if text[3] == 'v' else False
        places.append(Place(text[0], text[1], text[2], is_visited))
    in_file.close()
    return places


def display_list_of_places(places):
    """Display the list of places."""
    if len(places) == 0:
        print("No places to display")
    else:
        print("Places:")
        for i, place in enumerate(places):
            print(f"{i + 1}. {place}")


if __name__ == '__main__':
    main()

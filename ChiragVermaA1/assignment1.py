"""
Travel Tracker 1.0
Name: Chirag Verma
Date started: 31/03/2023
GitHub URL:
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
    places.sort(key=lambda place: (place[3], int(place[2])))
    print(f"{len(places)} places loaded from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        unvisited_places = [place for place in places if place[3] == 'n']
        if choice == 'L':
            display_list_of_places(places)
        elif choice == 'R':
            if len(unvisited_places) == 0:
                print("No places left to visit!")
            else:
                random_place_generator(unvisited_places)

        elif choice == 'A':
            pass
        elif choice == 'M':
            if len(unvisited_places) == 0:
                print("No unvisited places")
            else:
                display_list_of_places(places)
                mark_place_visited(places)

        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    print(f"{len(places)} saved to {FILENAME}")
    print("Have a nice day :)")


def mark_place_visited(places):
    print("Enter the number of a place to mark as visited")
    mark_number = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            mark_number = int(input(">>>"))
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
    randon_choice = random.choice(unvisited_places)
    print("Not sure where to visit next?")
    print("How about... {} in {}?".format(*randon_choice))


def load_data():
    in_file = open(FILENAME, "r")
    places = []
    for line in in_file:
        text = line[:-1].split(",")
        places.append(text)
    return places


def display_list_of_places(places):
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

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
    in_file = open(FILENAME, "r")
    places = []
    for line in in_file:
        text = line[:-1].split(",")
        places.append(text)
    print(places)
    print(f"{len(places)} places loaded from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            places.sort(key=lambda place: (place[3], int(place[2])))
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
        elif choice == 'R':
            unvisited_places = [place for place in places if place[3] == 'n']
            if len(unvisited_places) == 0:
                print("No places left to visit!")
            else:
                randon_choice = random.choice(unvisited_places)
                print("Not sure where to visit next?")
                print("How about... {} in {}?".format(*randon_choice))

        elif choice == 'A':
            pass
        elif choice == 'M':

        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    print(f"{len(places)} saved to {FILENAME}")
    print("Have a nice day :)")

    # for places in places:
    #     place[0], country, priority, corn = places
    #     print(place[0])


if __name__ == '__main__':
    main()

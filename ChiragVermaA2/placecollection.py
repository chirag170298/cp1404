""" PlaceCollection class."""

from place import Place


class PlaceCollection:
    """A collection of Place objects."""

    def __init__(self):
        """Construct an empty places list."""
        self.places = []

    def __str__(self):
        """Return string representation of the PlaceCollection object."""
        return "\n".join(str(place) for place in self.places)

    def load_places(self, filename):
        """Load and split data from FILENAME and store it into list."""
        with open(filename, "r") as in_file:
            for line in in_file:
                text = line[:-1].split(",")  # [-1] is for leave \n at the end of each line
                priority = int(text[2])
                is_visited = True if text[3] == 'v' else False
                place = Place(text[0], text[1], priority, is_visited)
                self.places.append(place)

    def save_places(self, filename):
        """Overwrite/save list places in file. """
        with open(filename, "w") as out_file:
            for place in self.places:
                visited_status = "v" if place.is_visited else "n"
                print(",".join([place.name, place.country, str(place.priority), visited_status]), file=out_file)

    def add_place(self, place: Place):
        """Add a new Place object to places list."""
        self.places.append(place)

    def number_of_unvisited_places(self):
        """Return the number of unvisited places from the list places. """
        return len([place for place in self.places if not place.is_visited])

    def sort(self, key):
        """Sort the lists by key passed to it and then by priority."""
        self.places.sort(key=lambda place: (getattr(place, key), place.priority))

    def __len__(self):
        """Returns the length of places."""
        return len(self.places)

    def __iter__(self):
        return iter(self.places)
""" """
from operator import attrgetter
from place import Place


class PlaceCollection:
    """"""

    def __init__(self):
        self.places = []

    def load_places(self, filename):
        """Load and split data from FILENAME and store it into list."""
        with open(filename, "r") as in_file:
            for line in in_file:
                text = line[:-1].split(",")  # [-1] is for leave \n at the end of each line
                priority = int(text[3])
                visited = True if text[3] == 'v' else False
                place = Place(text[0], text[1], priority, visited)
                self.places.append(place)

    def save_places(self, filename):
        """ """

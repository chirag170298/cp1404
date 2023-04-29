"""Place class with mark visited/unvisited and check importance methods."""


class Place:
    """Represent information about a place."""

    def __init__(self, name, country, priority, visited_status=False):
        """Construct a Place from the given values."""
        self.name = name
        self.country = country
        self.priority = priority
        self.visited_status = visited_status

    def __str__(self):
        """ Returns a string representation of place object."""
        return f"{self.name} in {self.country}, priority {self.priority}" + (
            "(visited)" if self.visited_status else "")

    def mark_visited(self):
        """Mark the place as visited."""
        self.visited_status = True

    def mark_unvisited(self):
        """Mark the place as unvisited."""
        self.visited_status = False

    def is_important(self):
        """Return True if a place is important i.e. priority less than or equal to 2 else False."""
        return self.priority <= 2

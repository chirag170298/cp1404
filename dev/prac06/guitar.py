"""the class"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of data in Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate the age of a guitar."""
        return 2023 - self.year

    def is_vintage(self):
        """Check if a guitar is vintage."""
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year

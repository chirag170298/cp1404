"""
estimated time: 20 min
actual time : 35 min
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0000):
        """Initialise a programming language values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of data in a programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if the language is dynamically typed."""
        return self.typing == "Dynamic"

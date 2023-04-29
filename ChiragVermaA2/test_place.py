"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place 1
    print("Test initial-value place 1:")
    new_place1 = Place("Malagar", "Spain", 1, False)

    # Write tests to show this initialisation works
    print(new_place1)

    # Test mark_visited function
    new_place1.mark_visited()
    print(new_place1)

    # Test initial-value place 2
    print("Test initial-value place 2:")
    new_place2 = Place("Mumbai", "India", 5, True)

    # Write tests to show this initialisation works
    print(new_place2)

    # Test mark_unvisited function
    new_place2.mark_unvisited()
    print(new_place2)

    # Test is_important method
    print("Is place 1 important: ", new_place1.is_important())
    print("Is place 2 important: ", new_place2.is_important())



run_tests()

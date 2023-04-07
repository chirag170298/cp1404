"""the tests"""

from dev.prac06.guitar import Guitar

g1 = Guitar("Gibson L-5 CES ", 1922, 16035)
g2 = Guitar("Another guitar", 2013, 5150)
print(g1)
print(f"{g1.name} get_age() - Expected 101. Got {g1.get_age()}")
print(f"{g2.name} get_age() - Expected 10. Got {g2.get_age()}")
print(f"{g1.name} is_vintage() - Expected True. Got {g1.is_vintage()}")
print(f"{g2.name} is_vintage() - Expected False. Got {g2.is_vintage()}")

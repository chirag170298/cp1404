

"""
q1. What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

a1. On line 1 I saw an output of randomly generated number between 5 and 20(inclusive).
    The smallest number i could have seen was 5, and the largest was 20.

q2. What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

a2. on line 2 I saw a randomly generated output between 3 and 10 with a step of 2.
    The smallest number I could have seen was 3, and the largest was 9.
    No, the only possible output will be odd numbers (3, 5, 7, 9) because it has a step size of 2.

q3. What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

a3. on line 3 I saw a randomly generated float number between 2.5 and 5.5.
    The smallest number I could have seen was 2.5, and the largest was 5.5.

q4. Program to produce a random number between 1 and 100.
"""

import random


def main():
    print(random.randint(1, 100))


main()

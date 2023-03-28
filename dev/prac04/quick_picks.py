"""
program that generate a quick pick.
"""
import random

MIN_NUM = 1
MAX_NUM = 45
NUMS_PER_LINE = 6

num_of_picks = int(input("How many numbers of quick picks you want? "))
for i in range(num_of_picks):
    quick_pick = []
    while len(quick_pick) < NUMS_PER_LINE:
        quick_pick_number = random.randint(MIN_NUM, MAX_NUM)
        if quick_pick_number not in quick_pick:
            quick_pick.append(quick_pick_number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))

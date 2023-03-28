"""Broken program to determine score status"""

import random


def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print("Result: ", result)

    random_score = random.randint(0, 100)
    result = calculate_result(random_score)
    print(f"For random score {random_score} result is {result}")


def calculate_result(score):
    """ return corresponding response to marks"""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent :)"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad :("


if __name__ == '__main__':
    main()

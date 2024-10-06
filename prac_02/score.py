"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    score = get_score()
    result = determine_grade(score)
    print(result)


def get_score():
    return float(input("Enter score: "))

def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

random_score = random.randint(0, 100)
random_result = determine_grade(random_score)
print(f"Random score result: {random_result}")

main()


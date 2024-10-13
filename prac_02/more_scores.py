
import random

def main():
    num_scores = int(input("Enter the number of scores: "))
    with open('results.txt', 'w') as file:
        for _ in range(num_scores):
            score = random.randint(0, 100)
            result = determine_grade(score)
            file.write(f"{score} is {result}\n")

    print(f" Here are results:")
    with open('results.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
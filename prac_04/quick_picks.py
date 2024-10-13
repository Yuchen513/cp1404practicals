import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join("{:2d}".format(num) for num in quick_pick))


def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)



main()
"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    num_months = int(input("How many months? "))
    incomes = [float(input(f"Enter income for month {month + 1}: ")) for month in range(num_months)]
    display_income_report(incomes)



def display_income_report(incomes):
    """This function will print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for index, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {index:2} - Income: ${income :10.2f} Total: ${total :10.2f}")


main()
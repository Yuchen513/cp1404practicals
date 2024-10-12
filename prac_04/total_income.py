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
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
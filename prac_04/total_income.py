"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for income_list over a given number of number_of_months."""
    income_list = []
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        income_list.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = income_list[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
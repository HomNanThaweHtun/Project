def main():
    """Display income report for incomes over a given number of month."""
    incomes = []
    month = int(input("How many month? "))

    for month in range(1, month + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_outcome(incomes, month)


def print_outcome(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for num_month in range(1, months + 1):
        income = incomes[num_month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(num_month, income, total))


main()
def main():
    price = float(input("Enter cents per kWh: "))
    daily_use = float(input("Enter daily use in kWh: "))
    number_of_days = int(input("Enter number of billing days: "))

    estimated_bill = (price * daily_use * number_of_days)/100

    print("Estimated bill: $", estimated_bill)

main()

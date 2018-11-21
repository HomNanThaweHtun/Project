def main():
    sales = float(input("Enter sales: $"))
    while (sales < 0):
        print("Invalid Choice.")
        sales = float(input("Enter sales: $"))
    if sales < 1000:
        user_bonus = sales * (10/100)
    elif sales >= 1000:
        user_bonus = sales * (15/100)
    print("User's bonus is: $", user_bonus)

main()

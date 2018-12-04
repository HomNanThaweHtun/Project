
import random
def main():

    MAX_INCREASE = 0.175  # 17.5%
    MAX_DECREASE = 0.05  # 5%
    MIN_PRICE = 1
    MAX_PRICE = 100.0
    INITIAL_PRICE = 10.0
    day_counter = []

    price = INITIAL_PRICE
    print("Starting price: ${:,.2f}".format(price))

    while price >= MIN_PRICE and price <= MAX_PRICE:
        price_change = 0
        # generate a random integer of 1 or 2
        # if it's 1, the price increases, otherwise it decreases
        if random.randint(1, 2) == 1:
            # generate a random floating-point number
            # between 0 and MAX_INCREASE
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # generate a random floating-point number
            # between negative MAX_DECREASE and 0
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        day_counter.append(price)
        for i in range(len(day_counter)):
            print("On day {0} the price is: ${1:,.2f}".format(i + 1, day_counter[i]))
    out_file = open("output.txt", 'w')
    for i in range(len(day_counter)):
        print("On day {0} the price is: ${1:,.2f}".format(i+1, day_counter[i], file=out_file))


main()
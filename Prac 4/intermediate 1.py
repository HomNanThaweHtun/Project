def main():
    numbers = []
    total = 0
    for i in range(5):
        get_num = int(input("Number : "))
        numbers.append(get_num)
        total += get_num

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[len(numbers)-1]))
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", total/len(numbers))



main()


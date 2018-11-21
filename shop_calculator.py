def main():
    discount = 0.9
    num=int(input("Enter number of items"))
    while(num < 0):
        print("Enter a positive number.")
        num = int(input("Enter number of items"))
    total = 0.0
    for i in range(0,num):
        price = float(input("Enter price of item"))
        total+=price
    print("Total price for",num,"items is", total)
    if (total>=100):
        total = discount*total
    print("Total price is ", total)
main()
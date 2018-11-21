def main():
firstnum = int(input("Enter the first number: "))
    secondnum = int(input("Enter the second number: "))
    count = 1
    for i in range (firstnum, secondnum+1):
        if(i%2 == 0):
            print(i, end=" ")
    print()

    for i in range (firstnum, secondnum+1):
        if(i%2 != 0):
            print(i, end=" ")
    print()

    for i in range(firstnum, secondnum + 1):
        while (count <= i):
            if(count*count == i):
                print(i, end=" ")
            count = count+1

        count = 1
    print()

main()
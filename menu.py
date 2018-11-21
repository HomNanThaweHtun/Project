def main():
    name = input("Enter name")
    print ("Hello"\n"GoodBye"\n"Quit")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit\n")
    while choice != "Q":
        if choice == "H":
            print("Hello ", user_name)
        elif choice == "G":
            print("Goodbye ", user_name)
        else:
            print("Invalid message")

        choice = input("(H)ello\n(G)oodbye\n(Q)uit\n")
    print "Thank you."
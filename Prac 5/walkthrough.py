# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD":"Queensland", "NSW": "New South Wales", "NT" :"Northern Territory", "WA" : "Western Australia", "ACT":"Australian Capital Territory", "VIC":"Victoria", "TAS":"Tasmania"}
# print(STATE_NAMES)
'''
state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state].format)
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
'''
for key,value in STATE_NAMES.items():
    print("{:4} is {}".format(key,value))

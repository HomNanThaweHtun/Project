COLOR_NAMES = {"ALICEBLUE": "#fof8ff", "ANTIQUEWHITE": "#faebd7" ,"ANTIQUEWHITE1": "#ffeefdb", "ANTIQUEWHITE2": "#eedfcc", "ANTIQUEWHITE3": "#cdc0b0", "ANTIQUEWHITE4": "#8b8378", "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6", "AQUAMARINE4": "458b74", "AZURE1": "#f0ffff"}

color = input("Enter the name of the color:").upper()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid short color")
    color = input("Enter the name of the color: ").upper()



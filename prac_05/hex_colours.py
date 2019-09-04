HEX_COLOURS = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "aquamarine4": "#458b74", "beige": "#f5f5dc",
               "blue1": "#0000ff", "BlueViolet": "#8a2be2", "brown1": "ff4040", "burlywood": "#deb887",
               "CadetBlue1": "#98f5ff", "chartreuse1": "7fff00"}

colour = input("Please enter a colour name")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")
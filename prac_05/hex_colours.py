"""
CP5632 Practical 5
Convert colour name to hex_code.
"""
COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Aquamarine": "#7fffd4",
               "Azure": "#f0ffff", "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000",
               "BlanchedAlmond": "#ffebcd", "Blue": "#0000ff"}

colour_name = input("Enter a colour name: ")
while colour_name!= "":
    for name, code in COLOUR_CODES.items():
        if colour_name.lower() == name.lower():
            print(f"{colour_name} is {code}")
            break
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ")
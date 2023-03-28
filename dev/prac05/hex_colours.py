"""Program that allows a user to enter a color and get the corresponding code."""

COLOR_TO_CODES = {"Amber": "ffbf00", "Aqua": "#00ffff", "Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2",
                  "Black": "#000000", "Bronze": "#cd7f32", "Brown": "#a52a2a", "Cream": "#fffdd0", "Crimson": "#dc143c",
                  "Green": "#00ff00"}

color = input("Enter a color name: ").title()
max_len = max(len(colour) for colour in list(COLOR_TO_CODES.keys()))
while color != "":
    try:
        print(f"{color:{max_len}} is {COLOR_TO_CODES[color]}")
    except KeyError:
        print("Invalid input")
    color = input("Enter a color name: ").title()



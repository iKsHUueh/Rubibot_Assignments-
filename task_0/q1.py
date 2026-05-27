face = ["red", "blue", "Red", "white", "RED", "blue", "White", "green", "Green"]
counts = {"R": 0, "B": 0, "W": 0, "G": 0}

for color in face:
    upper_color = color.upper()

    if upper_color == "RED":
        counts["R"] += 1
    elif upper_color == "BLUE":
        counts["B"] += 1
    elif upper_color == "WHITE":
        counts["W"] += 1
    elif upper_color == "GREEN":
        counts["G"] += 1

for initial, count in counts.items():
    print(f"{initial} appears {count} times")
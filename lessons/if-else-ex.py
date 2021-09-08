"""Challenge Question #1"""

choice: int = int(input("Enter a number: "))

# Implementing this logic
# Print A if choice < 25
# Print B if choice >= 25 and < 50
# Print C if choice > 75
# Print D if choice >= 50 and <= 75

if choice < 50:
    if choice > 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("C")
    else:
        print("D")
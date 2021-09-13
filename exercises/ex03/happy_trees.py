"""Drawing forests in a loop."""

__author__ = "730490857"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

i = 1

while i <= depth:
    print(TREE * i)
    i = i + 1
    

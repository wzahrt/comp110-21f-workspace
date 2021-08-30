"""Demonstrate how four numerical operators work in Python."""

__author__ = "730490857"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(left_hand_side ** right_hand_side))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(left_hand_side / right_hand_side))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(left_hand_side // right_hand_side))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(left_hand_side % right_hand_side))
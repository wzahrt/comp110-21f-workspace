"""Repeating a beat in a loop."""

__author__ = "730490857"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
beat_number: int = int(input("How many times do you want me to repeat it? "))
i: int = 0

if beat_number <= i:
    print("No beat...")
else:
    while i < 1:
        print(str(beat + " ") * (beat_number - 1) + beat)
        i = i + 1
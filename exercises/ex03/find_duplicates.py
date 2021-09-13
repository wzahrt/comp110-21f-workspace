"""Finding duplicate letters in a word."""

__author__ = "730490857"

word: str = input("Enter a word: ")

i: int = 0
number_of_letters: int = 0

while i < len(word):
    k: int = 0
    while k < len(word):
        if word[i] == word[k]:
            number_of_letters = number_of_letters + 1
            k = k + 1
        else:
            k = k + 1
    i = i + 1

number_of_letters = number_of_letters - len(word)
print("Found duplicates: " + str(number_of_letters >= 1))

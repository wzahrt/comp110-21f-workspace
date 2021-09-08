"""An example of conditional (if-else) statements."""

SECRET: int = 7

print("I am thinking of a number between 1-10, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!")
    print("Have an awesome rest of your day!")
else:
    print("Sorry you guessed incorrectly:/")
    if guess > SECRET:
        print("You guessed to high.")
    else:
        print("You guessed to low.")
print("Game over")